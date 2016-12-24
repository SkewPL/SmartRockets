# SmartRockets  
Simple example of the genetic alghorithm, written using Python 3.5 and PyGame. Based on [Daniel Shiffman's coding challenge](https://www.youtube.com/watch?v=bGz7mv2vD6g) which is based on [Jer Thorp's Smart Rockets](http://www.blprnt.com/smartrockets/).
  
Licence: Do whatever you want :)
  
## Game rules  
100 rockets starts at the bottom of the screen. Their goal is to fly to the target avoiding obstructions (and walls).
Fitness increases when rocket is closer to the target, and when rocket achieves the target - the time in what rocket achieved target is also added to the fitness.
When rocket crushes into wall or obstruction, fitness is divided by 10. Next generation begins when all rockets crushed, or we run out of genes (Default 10 000).
  
## Running example  
First off, make sure you have the dependencies:  
`pip install pygame`  
  
Then you can run the example simply by executing:  
`python run.py`  
  
To start simulation press SPACE. To remove all obstructions press D. To move target to the mouse position press T. To create obstruction, select first corner of the rectangle by pressing LPM, then second corner by again pressing LPM in another place. To create default obbstructions press D. To increase or decrease max tps press left or right bracket.
  
## Customize  
In the run.py file you can customize some variables:  
_max_tps_ - Maximum number of updates per second. 0 means unlimited. I recommend 100 if you want to see what's going on.  
_max_fps_ - Maximum number of rendering frames per second. Default 30.  
_lifespan_ - Number of genes, you can lower this to like 200 if you does not have a lot of obstructions, to increase performance.  
_rockets_ - Number of rockets in population, default 100. Increasing affects performance and memory usage a lot.  
  
When you minimize the window the drawing process pauses, so the simulation can be faster.