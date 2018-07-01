# Artificial-Idiot
Super intelligent(?) ViZdoom agent
SIST CS181 project
# Reinforcement Learning Materials

### Important Papers
https://openreview.net/pdf?id=Hk3mPK5gg ICLR2017 FAIR paper 2016 A3C+Curriculum <br>
https://arxiv.org/abs/1609.05521  Arnold CMU - DQRN + split network (Skill Learning?) <br>

### Curriculum Learning and Skill Learning
We need curriculum learning because the reward (e.g. kill an enemy) is too sparse at the training begining on complex tasks (deathmatch) <br>
https://arxiv.org/pdf/1705.06366.pdf BAIR paper for generating learning goals using GAN <br>
http://bair.berkeley.edu/blog/2017/12/20/reverse-curriculum/ Good blogs from BAIR <br>
https://www.ijcai.org/proceedings/2017/0757.pdf  IJCAI short paper <br>

### How to solve sparse reward and guide leaerning?
https://nlp.stanford.edu/pubs/liu2018reinforcement.pdf

### Reference Codes
https://github.com/glample/Arnold  Pytorch + Arnold <br>
https://github.com/mwydmuch/ViZDoom/blob/master/doc/Types.md ViZdoom APIdoc - Python <br>
https://github.com/flyyufelix/VizDoom-Keras-RL Tensorflow + Keras <br>


### Env
`tf-gpu==1.4.0, keras==2.1.6, scikit-image vizdoom`
suggest to use anaconda, create new env with pip
`conda create -n 'vizdoom' pip python=3.5`
and use pip install to install needed packages
### Usage
in experiments/drqn folder <br>
usage: <br>
`python drqn_curriculum.py -h`
