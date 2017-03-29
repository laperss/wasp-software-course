# Reflections

## Iteration 3
The overall git experience has been quite smooth so far. Making a new branch and merging it into the the master branch went well. One thing that surprised us was the visibility of the branches, since there is a clear distinction between a local branch and a global branch. After a branch is merged, the old branch needs to be manually cleaned up both on the git server and on the local git repository of the creator. We would like to improve the naming convention of the branches. At the moment we simply name it after the main feature that is implemented on that branch, but we could look into the git branching model by [Vincent Driessen](http://nvie.com/posts/a-successful-git-branching-model/). In this model a fixed number of branches are created which are reused over the course of the projet.

## Iteration 4
This iteration went less smooth than the previous iteration, due to difficulties with setting up the Travis configuration file. As it turns out, our build system requires python2 to be installed, while we only use python3. After some digging around we managed to go around this problem by forcing pip to install the package using a specified python version. To us it seems quite nice that you using Travis you can automatically test your code with many different configurations, since you might introduce bugs along the way that might not show up in all versions of our toolchain. We would not really do anything differently in this assignment, but in the future we would like to use pull requests together with Travis to ensure that everything is properly tested before merging. Another point that we would like to see a solution for is a testing framework like Travis, but for different types of hardware. We know that Google, Apple and Facebook use this to test their software on multiple phones, but it would be great if this could somehow also be done in embedded system and automation applications.

## Review of other team's code
We reviewed the [Chalmers group](https://github.com/pierg/wasp-secourse-lund) since they had also written their product in python. 
One thing that they had not integrated yet was correct punctuation, so we added this and made a pull request. We also identified additional bugs, where single letter words could not be correctly translated.

We also revied the [Lund group](https://github.com/chrinels/wasplund-software-PigLatin), which had quite a nice product. There were some issues in the documentation, which we made a pull request for. Additionally, we cleaned up some style issues in the code. 

## Final remarks 
The implementation of a simple python program using the different software tools have gone mostly smoothly. We were familiar with some of the tools from before, but others, like Travis, was the first time. 
Some parts of the exercise would have been more useful if we had not chosen to work in Python. Since Python is an interpreted language, the use of make files is not as important as when compiling e.g. in Java. Using buildit still improved the efficiency, but the code could easily have been done without it. Buildit did help when running test cases.
Some additional problems occured because of our usage of python. In particular in Iteration 4 we notices problems because of the way Travis ran code in different python versions. 

The usage of github's build-in functionality, such as issue tracking, helped us keeping track of what work to do. In a bigger project the benefits are certainly even bigger. Now we were only two so dividing work was not a problem. 
