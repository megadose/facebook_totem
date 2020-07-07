import argparse,csv,tqdm
from facebook_totem import *
parser = argparse.ArgumentParser()
parser.add_argument("--mode", help="There are different modes: single to get all ads on a page, multi to get the ads on different pages, search to search a page",required=True)
parser.add_argument("--url", help="The url of the target page (single mode)",required=False)
parser.add_argument("--urls", help="Csv file with the lists of the target urls (multi mode)",required=False)
parser.add_argument("--columns", help="The name of the column with the urls (multi mode)",required=False)
parser.add_argument("--target", help="Target name (search mode)",required=False)
parser.add_argument("--output", help="Name of the csv output file",required=True)
args = parser.parse_args()
if args.mode == "single":
    if args.url==None:
        print("The url of the target page are required in single mode !")
        exit()
    id = getIdFromUrl(args.url)
    result = getAdsFromId(id)
    if len(result)!=0:
        keys = result[0].keys()
        with open("output/"+str(args.output), 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            for data in result:
                writer.writerow(data)
        print("You can see the output in : output/"+str(args.output))
    else:
        print("Sorry, but this page hasn't used any ads")
        exit()
elif args.mode =="multi":
    if args.urls==None:
        print("A csv file with the lists of the target urls are required with multi mode !")
        exit()
    if args.columns==None:
        print("The name of the column with the urls are required with multi mode !")
        exit()
    targets=[]
    input_file = csv.DictReader(open(args.urls))
    for row in input_file:
        targets.append(row[args.columns])
    print(str(len(targets))+" targets found")
    for target in tqdm.tqdm(targets):
        username = target.split('.com/')[1].replace('/','')
        id = getIdFromUrl(target)
        result = getAdsFromId(id)
        if len(result)!=0:
            keys = result[0].keys()
            with open("output/"+str(username)+str(id)+".csv", 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=keys)
                writer.writeheader()
                for data in result:
                    writer.writerow(data)
        else:
            pass
    print("You can see the results in the output folder, if there is none it means that no page was found for any of the pages.\nThe pages that used ads have a file in the output folder.")
elif args.mode=="search":
    if args.target==None:
        print("The target name are required in search mode !")
        exit()
    result = getFacebookPageFromName(args.target)
    if len(result)!=0:
        keys = result[0].keys()
        with open("output/"+str(args.output), 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            for data in result:
                writer.writerow(data)
        print("You can see the output in : output/"+str(args.output))
    else:
        print("Sorry, no pages not found with this name")
        exit()
else:
    print("Check the help")
    exit()
