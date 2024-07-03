:: session 20.06.2024

::rem speek about git and github
::how to use --> git commit,  when or how , you have to write it in deteals
::how to use --> git push ,  normaly after week
::how to use --> git branch  , normaly to test idea im code parallel to the original code without bad effikt to the original
::search in google nach --> git branch
::example to see it  , create repo iwith the name:  store
git branch  rem to see the branches
git checkout -b orders   rem creating new branch
git branch   rem to see the branch
git checkout main        rem change to branch main
::you cant change from branch to other in any time , only after commit

::you have now 2 branches  how to joint them
::do merg at server
git pull

:: create rem new branch
git checkout -b payments   rem creating new branch name payments
git branch
:: make new txt file in payments
echo " b,nnb.,bn.,m" > text.txt
git add .
git commit 
:: pause 15 min

:: new project  to see how it works...........................
:: 1- make new folder  anaylisi
mkdir store
:: 2 open cmd from folder
cd store
:: start git in the folder store
get init
:: create txt file anaylisi.txt , thin add und commit it
git add .
git commit -m "add file"

:: 1- Now go to Github und creating new repo "store"
:: 2- do the three commands from githup in terminal cmd PS E:\Mystro\Mystro\store>

git remote add origin https://github.com/abattiasia/store.git
git branch -M main
git push -u origin main

::rem make new branch im local
git checkout -b copuns
::rem make txt file in terminal
echo " any bbgbhnkmkmk any" > any.txt
git add .
git commit -m "add copuns"
:: add img
git add .
git push   rem for first mal make problem. dann wiederhole mit dem neue command
git push --set-upstream origin anaylisi

:: Part 3: we have to Create a Pull Request
:: 1. Create a Pull Request:
:: ○ Go to the repository on GitHub.
::○ Click on the "Compare & pull request" button to create a pull request for your 
::r branch.
::r ○ Provide a meaningful title and description for your pull request.
:: ○ Submit the pull request.
::2. Review and Merge Pull Requests:
::○ The instructor or a designated reviewer will review the pull requests.
::○ Once approved, the pull requests will be merged into the main branch.
::3. Update Your Local Repository:
::After your pull request is merged, update your local repository to include the latest changes:
::sh
::Copy code
git checkout main
git pull origin main



::rREADME file how to write in README File
:: Example markdown cheat sheat
#Python
##
###
######
   Python
   print " hello World"
    rem go to google suche 