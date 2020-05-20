import java.util.*;
import java.io.*;

class ActivationFunction
{
	public static void main(String args[])
	{
		int i,j,k,n,m,sum,x=0,BinaryStep,BipolarStep;
		Scanner s=new Scanner(System.in);
		System.out.print("Enter the number of inputs: ");
		n=s.nextInt();
		int values[]=new int[n];
		int weights[]=new int[n];
		int identity[]=new int[n];
		double BinarySigmoid,Ex,BipolarSigmoid;
		System.out.println("Enter the values: ");
		for(i=0;i<n;i++)
		{
			values[i]=s.nextInt();
		}
		System.out.println("Enter the weights: ");
		for(i=0;i<n;i++)
		{
			weights[i]=s.nextInt();
		}
		for(i=0;i<n;i++)
		{
			identity[i]=values[i]*weights[i];
		}
		System.out.println("Identity Function: ");
		for(i=0;i<n;i++)
		{
			System.out.print(" "+identity[i]);
		}
		System.out.println();
		for(i=0;i<n;i++)
			x=x+identity[i];
		System.out.println("Summation: "+x);
		for(i=0;i<n;i++)
		{
			x=x+identity[i];
		}				
		if(x < 0)
			BinaryStep=0;
		else
			BinaryStep=1;
		Ex=Math.exp(x);
		System.out.println("Binary Step Function: "+BinaryStep);
		BinarySigmoid=Ex;
		System.out.println("Binary Sigmoid: "+BinarySigmoid);
		BipolarSigmoid=(1-Ex)/(1+Ex);
		System.out.println("Bipolar Sigmoid: "+BipolarSigmoid);
		if(x < 0)
			BipolarStep=-1;
		else
			BipolarStep=1;
		System.out.println("Bipolar Step: "+BipolarStep);
	
		
	}
}