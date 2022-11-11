int empty_value_sub(node e,int a)//a表示视角是玩家还是电脑 ，空格评分函数。 
{
	int temp=chessbored[e.i][e.j];
	chessbored[e.i][e.j]=a;
	if(near_num(e.i,e.j)>5)
	{
		chessbored[e.i][e.j]=temp;
		return fen_max;
	}
	chessbored[e.i][e.j]=temp;
	  int b=1,i,j,k,s=0,n,fa=black+white-a,b2=0;
	  for(k=1;k<6;k++)
	  {
			if(chessbored[e.i][e.j-k]==a)b*=4;
			else if(chessbored[e.i][e.j-k]<0)
			{				
				b2++;
				if(b2>1)
				{
					break;
				} 
				b*=2;					
			}
			else 
				break;
      }
      b2=0;
      for(k=1;k<6;k++)
	  {
			if(chessbored[e.i][e.j+k]==a)b*=4;
			else if(chessbored[e.i][e.j+k]<0)
			{
				b2++;
				if(b2>1)
				{
					break;
				} 
				b*=2;
			}
			else 
				break;
      }
   	  n=0;
      for(k=1;k<6&&chessbored[e.i][e.j-k]!=fa&&chessbored[e.i][e.j-k]!=side;k++)
 		n++;
	  for(k=1;k<6&&chessbored[e.i][e.j+k]!=fa&&chessbored[e.i][e.j+k]!=side;k++)
 		n++;
	  if(n<5)b=0;
	  if(n==5&&b==512)b=1024;
  	  s=s+b;
  	  
  	  b=1;b2=0;
  	  for(k=1;k<6;k++)
	  {
			if(chessbored[e.i-k][e.j]==a)b*=4;
			else if(chessbored[e.i-k][e.j]<0)
			{
				b2++;
				if(b2>1)
				{
					break;
				} 
				b*=2;
			}
			else 
				break;
      }
      b2=0;
      for(k=1;k<6;k++)
	  {
			if(chessbored[e.i+k][e.j]==a)b*=4;
			else if(chessbored[e.i+k][e.j]<0)
			{
				b2++;
				if(b2>1)
				{
					break;
				} 
				b*=2;
			}
			else 
				break;
      }
  	  n=0;
      for(k=1;k<6&&chessbored[e.i-k][e.j]!=fa&&chessbored[e.i-k][e.j]!=side;k++)
 		n++;
	  for(k=1;k<6&&chessbored[e.i+k][e.j]!=fa&&chessbored[e.i+k][e.j]!=side;k++)
 		n++;
	  if(n<5)b=0;
	  if(n==5&&b==512)b=1024;
  	  s=s+b;
  	  
  	  b=1;b2=0;
  	  for(k=1;k<6;k++)
	  {
			if(chessbored[e.i-k][e.j-k]==a)b*=4;
			else if(chessbored[e.i-k][e.j-k]<0)
			{
				b2++;
				if(b2>1)
				{
					break;
				} 
				b*=2;
			}
			else 
				break;
      }
      b2=0;
      for(k=1;k<6;k++)
	  {
			if(chessbored[e.i+k][e.j+k]==a)b*=4;
			else if(chessbored[e.i+k][e.j+k]<0)
			{
				b2++;
				if(b2>1)
				{
					break;
				} 
				b*=2;
			}
			else 
				break;
      }
  	  n=0;
      for(k=1;k<6&&chessbored[e.i-k][e.j-k]!=fa&&chessbored[e.i-k][e.j-k]!=side;k++)
 		n++;
	  for(k=1;k<6&&chessbored[e.i+k][e.j+k]!=fa&&chessbored[e.i+k][e.j+k]!=side;k++)
 		n++;
	  if(n<5)b=0;
	  if(n==5&&b==512)b=1024;
  	  s=s+b;
  	  
  	   b=1;b2=0;
  	  for(k=1;k<6;k++)
	  {
			if(chessbored[e.i-k][e.j+k]==a)b*=4;
			else if(chessbored[e.i-k][e.j+k]<0)
			{
				b2++;
				if(b2>1)
				{
					break;
				} 
				b*=2;
			}
			else 
				break;
      }
      b2=0;
      for(k=1;k<6;k++)
	  {
			if(chessbored[e.i+k][e.j-k]==a)b*=4;
			else if(chessbored[e.i+k][e.j-k]<0)
			{
				b2++;
				if(b2>1)
				{
					break;
				} 
				b*=2;
			}
			else 
				break;
      }
  	  n=0;
      for(k=1;k<6&&chessbored[e.i-k][e.j+k]!=fa&&chessbored[e.i-k][e.j+k]!=side;k++)
 		n++;
	  for(k=1;k<6&&chessbored[e.i+k][e.j-k]!=fa&&chessbored[e.i+k][e.j-k]!=side;k++)
 		n++;
	  if(n<5)b=0;
	  if(n==5&&b==512)b=1024;
  	  s=s+b;
  	  
  	  return s;
}
