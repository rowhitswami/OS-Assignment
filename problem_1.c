// Write a C program to create two zombie processes and two orphan processes using system calls.
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main()
{
    // Declaring and Forking Zombie Process
    pid_t zpid = fork();
    
    // Declaring and Forking Orphan Process
    pid_t opid = fork();
 
    // Parent process for zombie
    if (zpid > 0)
        sleep(5);
 
    // Child process for zombie
    else  {
        printf("(Zombie Process) Child exiting with process id %d because parent is sleeping.\n", getpid());
    }
    
    // Parent process for orphan
    if (opid > 0)
        printf("Parent Process with process id %d \n", getpid());
 
    // Child process for orphan process
    else if (opid == 0)
    {
        sleep(5);
        printf("(Orphan Process) Parent finishes execution and exits while the child process is still executing \n");
    }
 
    return 0;
}

