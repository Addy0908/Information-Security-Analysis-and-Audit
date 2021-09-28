#include<iostream>
#include<algorithm>

using namespace std;

class A
{
       public:
              string msg,key1,key2,enc1,decy1,enc2,decy2;
              int *ord1,*ord2,l1,l2;
              A (string s,string k1,string k2)
              {
                     msg = s;
                     key1 = k1;
                     key2 = k2;
                     l1 = k1.size();
                     l2 = k2.size();
                     ord1 = new int[l1];
                     ord2 = new int[l2];
              }
              void generate_Key(string s, int *p)
              {
                     int k = 1;
                     bool v[s.size()];
                     for(int i = 0;i<s.size();i++)
                     {
                           v[i] = false;
                     }
                     string t = s;
                     sort(s.begin(),s.end());
                     for(int i=0;i<s.size();i++)
                     {
                           for(int j=0;j<s.size();j++)
                           {
                                  if(s[i] == t[j]  && v[j] == false)
                                  {
                                         p[j] = k;
                                         v[j] = true;
                                         k++;
                                  }
                           }
                     }
                     cout<<endl;
              }
              string encrypt(string s, int *ord,int k)
              {
                     string str;
                     int c=1,f;
                     int l = s.size()/k;
                     char p;
                     for(int i=0;i<k;i++)
                     {
                           for(int j=0;j<k;j++)
                           {
                                  if(c==ord[j])
                                  {
                                         f = j;
                                         j = k;
                                         c++;
                                  }
                           }
                           for(int j=0;j<l+1;j++)
                           {
                                  if(j*k+f<s.size())
                                  {
                                         p = s[j*k+f];
                                  }
                                  else
                                  {
                                         p ='x';
                                  }
                                  str = str+ p;
                           }
                     }
                     cout<<str<<endl;
                     return str;
              }
              void B(string s, int *ord,int l)
              {
                     int z = s.size()/l;
                     z = (z+1)*l;
                     for(int i=0;i<l;i++)
                     {
                           cout<<"--";
                     }
                     cout<<endl;
                     for(int i=0;i<l;i++)
                     {
                           cout<<ord[i]<<" ";
                     }
                     cout<<endl;
                     for(int i=0;i<l;i++)
                     {
                           cout<<"--";
                     }
                     cout<<endl;
                     for(int i=0;i<z;i++)
                     {
                           if(i<s.size())
                           {
                                  cout<<s[i];
                           }
                           else
                           {
                                  cout<<"x";
                           }
                           if((i+1)%l==0)
                           {
                                  cout<<endl;
                           }
                           else
                           {
                                  cout<<" ";
                           }
                     }
                     for(int i=0;i<l;i++)
                     {
                           cout<<"--";
                     }
                     cout<<endl;
              }

};

int main()
{
       string s,k1,k2;
       cout<<"Enter The Message  that you want to encrypt: "<<endl;
       getline(cin,s);
       cout<<"Enter The First Key  for transposition: "<<endl;
       getline(cin,k1);
       cout<<"Enter The Second Key for transposition: "<<endl;
       getline(cin,k2);
       A d(s,k1,k2);

       cout<<"\nGenerating First Key : ";
       d.generate_Key(d.key1,d.ord1);
       d.B(d.msg,d.ord1,d.l1);
       cout<<" Ecrypting Message After Single Transposition : "<<endl;
       d.enc1 = d.encrypt(d.msg,d.ord1,d.l1);
       cout<<"\nGenerating Second Key : ";
       d.generate_Key(d.key2,d.ord2);
       d.B(d.enc1,d.ord2,d.l2);

       cout<<" Encrypting Message After Double Transposition : "<<endl;;
       d.enc2 = d.encrypt(d.enc1,d.ord2,d.l2);

       cout<<endl;
       return 0;
}
