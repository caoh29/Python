// imprime en la pantalla, el ; no es necesario pero se usa por conevncion y mejor practica
console.log('Hola, este es mi primer ejercicio con Node en el mejor Bootcamp de programación del mundo');

//se usa para llamar al modulo requiere para gestionar peticiones http
const http = require('http');

const host = '0.0.0.0';
const port = 3000;

const server = http.createServer(
    (req,res) => {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain')
        res.end('Peguelo chirrete xd')        
    } 
);

server.listen(port, host, ()=>{
    console.log('Server ON '+ host + '/'+ port)
});

