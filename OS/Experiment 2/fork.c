# include <sys/types.h>
# include <unistd.h>
# include <stdio.h>

void fork_id(){
    int f = fork();
    if (f < 0){
        printf("Forking failed!!!");
    }
    else if(f==0){
        printf("This is child process: \n");
        printf("Process id of child process : %d \n",getpid());
        printf("Parent process id of child process : %d \n", getppid());
    }
    else{
        printf("This is parent process: \n");
        printf("Process id of parent process : %d \n",getpid());
        printf("Parent process id of parent process : %d \n", getppid());
        printf("The value of fork : %d\n\n", f);
    }
}

int main(){
    fork_id();
}