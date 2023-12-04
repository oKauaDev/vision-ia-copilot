#!/bin/bash

# Função para instalar dependências
install_dependencies() {
    echo "Instalando dependências..."
    sudo apt update
    sudo apt install -y python3-dev python3-pip cmake libatlas-base-dev libhdf5-dev libhdf5-serial-dev libjasper-dev libqtgui4 libqt4-test
}

# Função para compilar o MediaPipe
compile_mediapipe() {
    echo "Clonando o repositório MediaPipe..."
    git clone https://github.com/google/mediapipe.git
    cd mediapipe

    echo "Atualizando submódulos..."
    git submodule update --init --recursive

    echo "Criando diretório de compilação..."
    mkdir build
    cd build

    echo "Configurando o ambiente para compilação..."
    cmake ..

    echo "Compilando o MediaPipe..."

    # Configuração da barra de progresso
    length=50
    percent=0
    progress=""
    
    for ((i=0; i<=length; i++)); do
        progress+=" "
    done

    for ((i=0; i<=length; i++)); do
        percent=$((i * 2))
        echo -ne "[$progress] $percent%\r"
        make -j4 > /dev/null 2>&1
        progress="#$progress"
        sleep 0.1
    done

    echo -e "\nCompilação concluída."
}

# Início da execução do script
echo "Script de compilação do MediaPipe"

# Executa a instalação de dependências
install_dependencies

# Executa a compilação do MediaPipe
compile_mediapipe
