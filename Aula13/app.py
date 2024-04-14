
#Geral: pacote instalado:pip install beautifulsoup4 geral
#\na app em uso: entrar na pasta do arquivo que vai usar a lib e digitar
# pip install beautifulsoup4 -t ./libs
# remover um pacote subistituir install por unistall
#pode tambem criar um arquivo com o nome exemplo requirements.txt e fazer como acima subistituindo o beautifulsoup4 
#por ele no comando e nele pode aver N pacotes listados, todos serão instalados 
import tools 

print(tools.PI)
print(tools.GRAVITY)
print(tools.get_extensions("teste.txt"))
print(tools.highest_number([1,2,3,4,5,6,7,8,9]))