with open("requirements.txt","r") as fread:
    reqs=[x.split('==')[0] for x in fread.read().split('\n') if "git+https" not in x and "0.0.0" not in x]
with open("install_reqs.sh","w") as fwrite:
    fwrite.write("poetry add --allow-prereleases "+" ".join(reqs))