// write a code for FCFS scheduling algorithm
#include<stdio.h>
int main()
{
    int n, i, temp, sum = 0, wait = 0, intTat = 0;
    float avg_wait, avg_tat;
    printf("Enter the number of processes: ");
    scanf("%d", &n);
    int bt[n], wt[n], tat[n];
    printf("Enter the burst time of the processes: \n");
    for(i = 0; i < n; i++)
    {
        scanf("%d", &bt[i]);
    }
    wt[0] = 0;
    for(i = 1; i < n; i++)
    {
        wt[i] = wt[i-1] + bt[i-1];
    }
    for(i = 0; i < n; i++)
    {
        tat[i] = wt[i] + bt[i];
    }
    for(i = 0; i < n; i++)
    {
        wait = wait + wt[i];
        intTat = intTat + tat[i];
    }
    avg_wait = (float)wait/n;
    avg_tat = (float)intTat/n;
    printf("Process\tBurst Time\tWaiting Time\tTurn Around Time \n");
    for(i = 0; i < n; i++)
    {
        printf("%d\t%d\t\t%d\t\t%d \n", i+1, bt[i], wt[i], tat[i]);
    }
    printf("Average waiting time: %f \n", avg_wait);
    printf("Average turn around time: %f \n", avg_tat);
    return 0;
}
