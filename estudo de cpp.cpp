#include <iostream>
using namespace std;

class propaganda{
    private:
    
    public:
    void inscrever(){
        cout<<"Se inscreva no canal!\n";
    }
    void curtir(){
        cout<<"Deixa o like no video!\n";
    }
};

class carro{
    private:
    
    int ano;
    double preco, km;
    
    public:
    
    // construtor -> função que serve para quando o objeto for criado ele já inicie "com alguma coisa"
    // função construtor não precisa do tipo de saída E recebe o mesmo nome da classe
    
    carro(int a, float p, float k){// poderia ser (inta=0) -> significa que se o valor a não for informado no parâmetro ele inicia zerado
        ano  = a;
        preco = p;
        km = k;
    } 
    
    // no caso acima, ao ser criado um objeto ele já deve fornecer os valores de parâmetros (ano, preco e km) sem necessidade de ficar
    // usando set's
    
    // ao ser criado o objeto automaticamente o construtor é criado 
    
    //get e set (get obter algo, set "indicar algo")
    
    void setano(int a){
        ano = a;
        //this->ano = ano (O this é usado no caso de o parâmetro da função ser igual ao atributo privado, ex: ano e ano; o this indica o private)
    }
    int getano(){
        return ano;
    }
};

int main(){
  propaganda Canal;
  Canal.inscrever();
  Canal.curtir();
  
  //carro Fusca;
  //Fusca.setano(1980);
  //cout<<"\n"<<Fusca.getano()<<endl;
  
  carro Palio(1995,1000,150000);
  cout<<"Palio:\n";
  cout<<"Ano: "<<Palio.getano()<<endl;
}