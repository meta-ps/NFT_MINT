from django.shortcuts import render,redirect
import requests
import json
import os
from config.settings import BASE_DIR
from pathlib import Path
import shutil
from pathlib2 import Path as Path2_
from pathlib import Path

# Create your views here.
def Home(request):
    request.session['WalletAddress'] = "xxx"
    if request.POST:
        walletAddress = request.POST.get('WalletAddress')
        request.session['WalletAddress'] = walletAddress
        imageurl=request.POST.get('imgurl')
        path =Path(os.path.normpath( str(BASE_DIR) + '/'+ 'NFT.sol'))
        path2 =Path(os.path.normpath( str(BASE_DIR) +'/contracts/NFT.sol'))

        shutil.copyfile(path,path2)

        file = Path2_(path2)
        data = file.read_text()
        data = data.replace("USER_ADDRESS", walletAddress)
        file.write_text(data)
        
        file = Path2_(path2)
        data = file.read_text()
        data = data.replace("TOKENURI", imageurl)
        file.write_text(data)


        try:
            shutil.rmtree("contracts/artifacts")
            shutil.rmtree("contracts/cache")
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))


        os.system("npx hardhat run scripts/deploy.js --network mumbai")
        #https://mumbai.polygonscan.com/tx/0x6edaec6b1751c0de86f89594d18e21af59d781216be79f64e0d269c76d30e976
        #https://mumbai.polygonscan.com/tx/0x6edaec6b1751c0de86f89594d18e21af59d781216be79f64e0d269c76d30e976
        q = open('address.txt','r')
        pqrq=q.read()
        print(pqrq)
        
        deployed_url = "https://mumbai.polygonscan.com/tx/"+str(pqrq)
        request.session['polygonscan'] = deployed_url
        print('xxxxxxxxxxxxxxxxxxx')
        print(deployed_url)
        shutil.copyfile(path,path2)

        

        return redirect('nftUpload')

    context = {}
    return render(request,'home.html',context)


def nftUpload(request):
    deployed_url=request.session['polygonscan']
    return render(request,'sucess.html',{'deployed_url':deployed_url})