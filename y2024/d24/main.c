#include <stdbool.h>
#include <string.h>
#include <time.h>
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#define INF (1LL<<62)
#define RULES_LEN 222
#define TS_LEN 20
#define FILTER_RATE 0.1
#define BRUTE_THRESH 50
bool flags[RULES_LEN],*par;
int valc,zbvm[46],defsco[RULES_LEN*RULES_LEN],scores_s[RULES_LEN*RULES_LEN],scores_n[RULES_LEN*RULES_LEN],*vals,**rules;
long long ts[TS_LEN][2];
void mergesort(long long *a,int l,int r){
    if(l+1>=r)
        return;
    int mid=(l+r)/2;
    mergesort(a,l,mid);
    mergesort(a,mid,r);
    long long *t=malloc((r-l)*sizeof(long long));
    int i=l;
    int j=mid;
    int k=0;
    while(i<mid||j<r) {
        while(i<mid&&(j>=r||a[i]<=a[j]))
            t[k++]=a[i++];
        while(j<r&&(i>=mid||a[j]<=a[i]))
            t[k++]=a[j++];
    }
    for(int i=l;i<r;i++)
        a[i]=t[i-l];
    free(t);
}
int c2n(char c){
    return (c<'a')?(c-'0'):(c-'a'+10);
}
char n2c(int n){
    return (n<10)?(n+'0'):(n+'a'-10);
}
int s2n(char *s){
    return c2n(s[2])+36*c2n(s[1])+36*36*(c2n(s[0]));
}
void n2s(char *s,int n){
    s[0]=n2c(n/36/36);
    s[1]=n2c((n/36)%36);
    s[2]=n2c(n%36);
}
bool dfs(int v){
    if(vals[v]>-1)
        return false;
    if(par[v])
        return true;
    par[v]=true;
    for(int i=1;i<3;i++){
        if(dfs(rules[v][i]))
            return true;
    }
    switch(rules[v][0]){
    case 'X':
        vals[v]=vals[rules[v][1]]^vals[rules[v][2]];
        break;
    case 'A':
        vals[v]=vals[rules[v][1]]&vals[rules[v][2]];
        break;
    case 'O':
        vals[v]=vals[rules[v][1]]|vals[rules[v][2]];
        break;
    default:
        assert(false);
    }
    par[v]=false;
    return false;
}
long long compute_Z(long long *XY){
    memset(par,false,valc);
    memset(vals,-1,valc*sizeof(int));
    for(int i=0;i<2;i++){
        for(int j=0;j<45;j++)
            vals[45*i+j]=(XY[i]>>j)&1;
    }
    long long Z=0;
    for(int i=0;i<46;i++){
        if(dfs(zbvm[i]))
            return INF;
        Z|=((long long)vals[zbvm[i]])<<i;
    }
    return Z;
}
void gen_testset(void){
    for(int i=0;i<TS_LEN;i++){
        for(int j=0;j<2;j++)
            ts[i][j]=(((long long)rand())<<14)^((long long)rand());
    }
}
void gen_perm(int *perm,int st,const int *cands,int candc){
    for(int i=0;i<st;i++)
        flags[perm[i]/RULES_LEN]=flags[perm[i]%RULES_LEN]=true;
    for(int i=st;i<4;){
        perm[i]=cands[rand()%candc];
        if(flags[perm[i]/RULES_LEN]||flags[perm[i]%RULES_LEN])
            continue;
        flags[perm[i]/RULES_LEN]=flags[perm[i]%RULES_LEN]=true;
        i++;
    }
    for(int i=0;i<4;i++)
        flags[perm[i]/RULES_LEN]=flags[perm[i]%RULES_LEN]=false;
}
long long get_err(long long mx){
    long long err=0;
    for(int i=0;i<TS_LEN;i++){
        long long act=compute_Z(ts[i]);
        if(act==INF)
            return INF;
        err+=__builtin_popcountll((ts[i][0]+ts[i][1])^act);
        if(err>mx)
            return err;
    }
    return err;
}
void swap_rules(int i,int j){
    int t[3];
    memcpy(&t,rules[i],sizeof(t));
    memcpy(rules[i],rules[j],sizeof(t));
    memcpy(rules[j],&t,sizeof(t));
}
void swap_perm(const int *perm){
    for(int i=0;i<4;i++)
        swap_rules(perm[i]/RULES_LEN+90,perm[i]%RULES_LEN+90);
}
long long get_err4perm(const int *perm,long long mx){
    swap_perm(perm);
    long long err=get_err(mx);
    swap_perm(perm);
    return err;
}
bool brute(int *pairs,int dep,int st,const int *cands,int candc){
    if(dep<4){
        for(int i=st;i<candc;i++){
            if(flags[cands[i]/RULES_LEN]||flags[cands[i]%RULES_LEN])
                continue;
            flags[cands[i]/RULES_LEN]=flags[cands[i]%RULES_LEN]=true;
            pairs[dep]=cands[i];
            if(brute(pairs,dep+1,i+1,cands,candc))
                return true;
            flags[cands[i]/RULES_LEN]=flags[cands[i]%RULES_LEN]=false;
        }
        return false;
    }
    return !get_err4perm(pairs,0);
}
int main(void){
    srand(time(NULL));
    char line[20];
    int n2cn[36*36*36];
    memset(n2cn,-1,sizeof(n2cn));
    long long XY[2];
    XY[0]=XY[1]=0;
    while(fgets(line,sizeof(line),stdin)&&line[0]!='\n'){
        XY[line[0]=='y']|=((long long)(line[5]-'0'))<<(10*((int)(line[1]-'0'))+((int)(line[2]-'0')));
        n2cn[s2n(line)]=valc++;
    }
    int raw_rules[RULES_LEN][4];
    for(int i=0;fgets(line,sizeof(line),stdin)&&line[0]!='\n';i++){
        raw_rules[i][0]=line[4];
        raw_rules[i][1]=s2n(line);
        raw_rules[i][2]=s2n(line+7+(line[4]!='O'));
        raw_rules[i][3]=s2n(line+14+(line[4]!='O'));
        n2cn[raw_rules[i][3]]=valc++;
        if(line[14+(line[4]!='O')]=='z')
            zbvm[10*((int)(line[15+(line[4]!='O')]-'0'))+((int)(line[16+(line[4]!='O')]-'0'))]=n2cn[raw_rules[i][3]];
    }
    par=malloc(valc);
    vals=malloc(valc*sizeof(int));
    rules=malloc(valc*sizeof(int*));
    for(int i=0;i<RULES_LEN;i++){
        rules[n2cn[raw_rules[i][3]]]=malloc(3*sizeof(int));
        rules[n2cn[raw_rules[i][3]]][0]=raw_rules[i][0];
        for(int j=1;j<3;j++)
            rules[n2cn[raw_rules[i][3]]][j]=n2cn[raw_rules[i][j]];
    }
    long long ans1=compute_Z(&XY[0]);
    gen_testset();
    int candc,*cands;
    candc=0;
    cands=malloc(RULES_LEN*(RULES_LEN-1)/2*sizeof(int));
    for(int i=90;i<valc;i++){
        for(int j=i+1;j<valc;j++){
            swap_rules(i,j);
            if(get_err(INF)<INF)
                cands[candc++]=(i-90)*RULES_LEN+j-90;
            swap_rules(i,j);
        }
    }
    for(int i=0;i<candc;){
        int perm[4];
        perm[0]=cands[i];
        gen_perm(perm,1,cands,candc);
        long long err=get_err4perm(perm,INF);
        if(err==INF)
            continue;
        defsco[cands[i]]=(int)err;
        i++;
    }
    while(candc>BRUTE_THRESH){
        for(int i=0;i<candc;i++){
            scores_s[cands[i]]=defsco[cands[i]];
            scores_n[cands[i]]=1;
        }
        for(int i=0;i<50000;){
            int perm[4];
            gen_perm(perm,0,cands,candc);
            long long err=get_err4perm(perm,INF);
            if(err==INF)
                continue;
            for(int j=0;j<4;j++){
                scores_s[perm[j]]+=err;
                scores_n[perm[j]]++;
            }
            i++;
        }
        long long *tosort=malloc(candc*sizeof(long long));
        for(int i=0;i<candc;i++)
            tosort[i]=(((((long long)scores_s[cands[i]])<<30)/scores_n[cands[i]])<<20)|cands[i];
        mergesort(tosort,0,candc);
        int ncc=0;
        while((ncc+1)<candc*(1-FILTER_RATE)){
            cands[ncc]=tosort[ncc]&((1<<20)-1);
            ncc++;
        }
        free(tosort);
        candc=ncc;
    }
    int pairs[4];
    assert(brute(pairs,0,0,cands,candc));
    long long involved[8];
    for(int i=0;i<4;i++){
        involved[2*i]=raw_rules[pairs[i]/RULES_LEN][3];
        involved[2*i+1]=raw_rules[pairs[i]%RULES_LEN][3];
    }
    mergesort(involved,0,8);
    char ans2[32];
    for(int i=0;i<8;i++){
        n2s(ans2+4*i,involved[i]);
        ans2[4*i+3]=',';
    }
    ans2[31]='\0';
    printf("%lld %s\n",ans1,ans2);
    return 0;
}

