### This is a developer guide on some of the basic git commands that we will be using

####Retrieving changes from someone else's branch:
These are the steps I went through to get Sarthak's changes 
from his branch onto mine, bypassing the master branch.
Generally speaking, we shouldn't really be accessing code on each others 
branches but as the functionality isn't complete, the html shouldn't really be in master 
yet. So we'll treat this as the exception.

1. ```git fetch``` - to get any recent changes
2. ```git branch``` - check that you are on your branch
3. ```git checkout sarthakkapoor``` - to checkout to Sarthak's branch (we're doing this to get 
local copy of Sarthak's branch)
4. ```git checkout <yourbranchname>``` - to switch back you your branch 
5. ```git merge sarthakkapoor``` - to now merge Sarthak's branch with your own
6. You should now have the changes to html/ css in your branch

_Note: This isn't necessarily the best way of doing this but it does work._
