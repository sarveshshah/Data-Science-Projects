import static java.lang.Math.sqrt;
import java.util.Random;
import java.util.Scanner;

public class kmeans {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        Random r=new Random();
        int dx[]=new int[200];
        int dy[]=new int[200];
        int dclass[]=new int[200];
        //Initialized data points 
        for (int i = 0; i < dy.length; i++) {
             dy[i]=r.nextInt(150);
             dx[i]=r.nextInt(150);
        }
        int k=3; //number of clusters
        int cx[]=new int[k]; //Center for the cluster
        int cy[]=new int[k];
        int dist[][]=new int[cy.length][k];
        int sum1x=0,sum2x=0,sum3x=0,sum1y=0,sum2y=0,sum3y=0;
        int c1x=0,c2x=0,c3x=0,c1y=0,c2y=0,c3y=0;
        //int[] cluster=new int[k];
        int count=0;
        for (int i = 0; i < k; i++) {
            cx[i]=r.nextInt(200); //first iteration random centers assigned
            cy[i]=r.nextInt(200);   
        }
        int epoch=0;
        while(epoch<20)
        {     
            for (int i = 0; i < dy.length; i++) {
                while(count<k)     
                   dist[i][k]=dis(dx[i],dy[i],cx[k],cy[k]);
                count=0;              
            if(dist[i][0]>dist[i][1]&&dist[i][0]>dist[i][2])
                dclass[i]=1;
            else if(dist[i][0]>dist[i][1]&&dist[i][0]<dist[i][2])
                dclass[i]=3;
            else
                dclass[i]=2;
            }
            for (int i = 0; i < dy.length; i++) {
                if(dclass[i]==1)
                    {
                       sum1x+=dx[i];
                       sum1y+=dx[i];
                       c1x++;
                       c1y++;
                    }
                if(dclass[i]==2)
                    {
                       sum2x+=dx[i];
                       sum2y+=dx[i];
                       c2x++;
                       c2y++;
                    }
                if(dclass[i]==3)
                    {
                       sum3x+=dx[i];
                       sum3y+=dx[i];
                       c3x++;
                       c3y++;
                    }  
            }
            //allocating new centers
            cx[0]=sum1x/c1x;
            cx[1]=sum2x/c2x;
            cx[2]=sum3x/c3x;
            cy[0]=sum1y/c1y;
            cy[1]=sum2y/c2y;
            cy[2]=sum3y/c3y;
            epoch++;
        }
        for (int i = 0; i < dy.length; i++) 
            System.out.println("The point "+dx[i]+" "+dy[i]+" belongs to "+" cluster "+dclass[i]);    
    }
    
public static int dis(int dx,int dy,int cx,int cy)
    {
        int Dx=0,Dy=0;
        Dy=(dy-cy)*(dy-cy);
        Dx=(dx-cx)*(dx-cx);
        return (int) sqrt(Dx+Dy);
    }
}

