import random

def get_pi_montecarlo(throw_count):
    in_circle=0
    out_circle=0
    for i in range(throw_count):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        if ((x**2)+(y**2))**(1/2)>1:
            out_circle+=1
        else:
            in_circle+=1
    return 4*(in_circle/throw_count)

print(get_pi_montecarlo(99))

