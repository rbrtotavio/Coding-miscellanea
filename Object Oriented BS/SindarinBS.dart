class Humanoide {
  String nome;
  num lvl;

  Humanoide(this.nome, this.lvl);

  void describe() {
    print('\nNome:$nome, Nível:$lvl.');
  }
}

class Elf extends Humanoide {
  String passive;

  Elf(String nome, num lvl, this.passive)
      :super(nome, lvl);

  void describe(){
    super.describe();
    print('Passiva Élfica:$passive.');
  }
}

class Dwarf extends Humanoide {
  String weapon;

  Dwarf(String nome, num lvl, this.weapon)
      :super(nome, lvl);

  void describe(){
    super.describe();
    print('Arma Anã:$weapon.');
  }
}

var elfo = Elf('Aglarinn', 55, 'Resistência à Magia');

var anao = Dwarf('Balin', 65, 'Machado Gigante');

void main(){
  elfo.describe();
  anao.describe();
  print('\nCANCELA O BABU NÃO, CARALHO!');
}