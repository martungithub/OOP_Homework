#include <stdio.h>
#include <time.h> 

typedef struct {
    int shinning ;
    int t_sunshine;
    int t_sunset;
} Sun;

typedef struct {
    int eating;
    int moving;
    int sleeping;
    int breathing;
} Frog;

typedef struct {
    int green;
} Grass;

typedef struct {
    int produce;
} Tree;


void sun_construct(Sun* sun) {
    sun->shinning = 0;
    sun->t_sunshine = 10;
    sun->t_sunset = 5;
}

void frog_construct(Frog* frog) {
    frog->eating = 0;
    frog->moving = 0;
    frog->sleeping = 1;
    frog->breathing = 0;
}

void grass_construct(Grass* grass) {
    grass->green = 10;
}
void tree_construct(Tree* tree) {
    tree->produce = 0;
}   

void frog_behavior(Sun * sun, Frog * frog){
    if (sun->shinning == 1){
        frog->eating = 1;
        frog->moving = 1;
        frog->breathing = 1;
        frog->sleeping = 0;
        printf("Frog is moving, eating and breathing.\n");
    }
    else{
        printf("Frog is sleeping.\n");
    }
}
void tree_behavior(Sun * sun, Tree * tree){
    if (sun->shinning == 1){
        tree->produce = 1;
        printf("Tree produces oxygen.\n");
    }
    else{
        
        printf("Tree does not produce oxygen.\n");


    }
}
void sun_behavior(Sun * sun){
    if(sun->t_sunshine >= 7){
        printf("Sun is shinning\n");
        sun->shinning = 1;
    }
    else{
        sun->shinning = 0;
        printf("Sun is not shinning\n");
    }
}

    

    
int main() {
    
    Sun sun;
    Tree tree;
    Frog frog;
    Grass grass;
    
    sun_construct(&sun);
    tree_construct(&tree);
    frog_construct(&frog);
    grass_construct(&grass);
    

    while(sun.t_sunshine > -1)
    {
      if (sun.t_sunshine != 0)
      {
        sun_behavior(&sun);
        tree_behavior(&sun, &tree);
        frog_behavior(&sun, &frog);
        sun.t_sunshine--;
        sleep(3);
    
      if(sun.t_sunshine < 5)
      {
        sun.t_sunshine-- ;
      }
      }
    }


    return 0;
}