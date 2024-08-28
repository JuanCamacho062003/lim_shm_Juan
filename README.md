# lim_shm_Juan
Este repositorio corresponde a la clase de sistemas inteligentes de la U.ECCI
## Intalacion de ollama
2. Para intalar ollama accedemos a la pagina de: [ollama](https://ollama.com/ )

```
$curl -fssl https://ollama.com/install.sh | sh
```
## 2. Ejecutar el servidor
una vez instalado se ejecutara el servidor ollama con el siguiente comando

````
$ ollama serve
````

## 3. Descargar algun modelo
En la pagina de [modelos](https://ollama.com/library) de ollama se busca el modelo deseado y se descarga con el sigueinte comando

```
$ ollama pull tinyllama
```

## 4. Comandos de Git
```
1. "Git add. ": Este comando añade todos los archivos nuevos, modificados o eliminados en el directorio actual y sus subdirectorios al área de preparación

2. "Git Commit -m "Update Readme.md" : Aqui subimos cambios a la rama y lo que se cuentra entre comillas es el nombre del commit

3. "Git comando git push -u origin main":  Se usa para subir (o "empujar") tus commits locales al repositorio remoto en la rama main.

4. "Git config --global" se utiliza para configurar opciones globales de Git que se aplican a todos los repositorios en tu sistema.
    * git config --global user.email "tu.email@example.com"
    * git config --global user.name "Tu Nombre"
```


