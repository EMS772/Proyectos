using Tienda_NetCore.Models.Entidades;

namespace Tienda_NetCore.Models.Data
{
    public class DataSeeder
    {
        private readonly TiendaContext _context;

        public DataSeeder(TiendaContext context)
        {
            _context = context;
        }

        public void Seed()
        {
            SeedCategorias();
            SeedProductos();
        }

        private void SeedCategorias()
        {
            if (!_context.Categorias.Any())
            {
                var categorias = new List<Categoria>
                {
                    new Categoria { Nombre = "Deportes" },
                    new Categoria { Nombre = "Electrónica" },
                    new Categoria { Nombre = "Hogar" }
                };

                _context.Categorias.AddRange(categorias);
                _context.SaveChanges();
            }
        }

        private void SeedProductos()
        {
            if (!_context.Productos.Any())
            {
                var categorias = _context.Categorias.ToList();
                var deportesId = categorias.First(c => c.Nombre == "Deportes").Id;
                var electronicaId = categorias.First(c => c.Nombre == "Electrónica").Id;
                var hogarId = categorias.First(c => c.Nombre == "Hogar").Id;

                var productos = new List<Producto>
                {
                    new Producto
                    {
                        Nombre = "Jordan 1 Blanco/Negro",
                        Descripcion = "Jordan 1 en su versión Blanco/Negro! Estas zapatillas combinan un diseño clásico con una paleta de colores atemporal que se adapta a cualquier estilo.",
                        Precio = 200,
                        ImagenUrl = "gs://twecommerce-14b8f.appspot.com/Fotos_Perfil/Jordan's.png",
                        CategoriaId = deportesId
                    },
                    new Producto
                    {
                        Nombre = "Monitor",
                        Descripcion = "Monitor de alta resolución",
                        Precio = 150,
                        ImagenUrl = "gs://twecommerce-14b8f.appspot.com/Fotos_Perfil/monitor.png",
                        CategoriaId = electronicaId
                    },
                    new Producto
                    {
                        Nombre = "Alfombra",
                        Descripcion = "Alfombra suave y cómoda",
                        Precio = 50,
                        ImagenUrl = "gs://twecommerce-14b8f.appspot.com/Fotos_Perfil/Alfombra.png",
                        CategoriaId = hogarId
                    },
                    new Producto
                    {
                        Nombre = "Mochila",
                        Descripcion = "Mochila resistente y espaciosa",
                        Precio = 70,
                        ImagenUrl = "gs://twecommerce-14b8f.appspot.com/Fotos_Perfil/mochila.png",
                        CategoriaId = deportesId
                    },
                    new Producto
                    {
                        Nombre = "Air Force Ones Blancos",
                        Descripcion = "Zapatos clásicos Air Force Ones en color blanco",
                        Precio = 120,
                        ImagenUrl = "gs://twecommerce-14b8f.appspot.com/Fotos_Perfil/Nikes Blancos.png",
                        CategoriaId = deportesId
                    },
                    new Producto
                    {
                        Nombre = "PS4",
                        Descripcion = "Consola de videojuegos PlayStation 4",
                        Precio = 300,
                        ImagenUrl = "gs://twecommerce-14b8f.appspot.com/Fotos_Perfil/ps4.png",
                        CategoriaId = electronicaId
                    },
                    new Producto
                    {
                        Nombre = "Reloj",
                        Descripcion = "Reloj elegante y moderno",
                        Precio = 100,
                        ImagenUrl = "gs://twecommerce-14b8f.appspot.com/Fotos_Perfil/reloj.png",
                        CategoriaId = hogarId
                    },
                    new Producto
                    {
                        Nombre = "Sábanas",
                        Descripcion = "Juego de sábanas suaves",
                        Precio = 40,
                        ImagenUrl = "gs://twecommerce-14b8f.appspot.com/Fotos_Perfil/Sabanas.png",
                        CategoriaId = hogarId
                    },
                    new Producto
                    {
                        Nombre = "Televisor",
                        Descripcion = "Televisor de alta definición",
                        Precio = 500,
                        ImagenUrl = "gs://twecommerce-14b8f.appspot.com/Fotos_Perfil/televisor.png",
                        CategoriaId = electronicaId
                    },
                    new Producto
                    {
                        Nombre = "Tocador",
                        Descripcion = "Tocador con espejo y cajones",
                        Precio = 200,
                        ImagenUrl = "gs://twecommerce-14b8f.appspot.com/Fotos_Perfil/tocador.png",
                        CategoriaId = hogarId
                    },
                    new Producto
                    {
                        Nombre = "Mesa",
                        Descripcion = "Mesa de comedor moderna",
                        Precio = 150,
                        ImagenUrl = "gs://twecommerce-14b8f.appspot.com/Fotos_Perfil/mesa.png",
                        CategoriaId = hogarId
                    },
                    new Producto
                    {
                        Nombre = "Closet",
                        Descripcion = "Closet espacioso",
                        Precio = 300,
                        ImagenUrl = "gs://twecommerce-14b8f.appspot.com/Fotos_Perfil/closet.png",
                        CategoriaId = hogarId
                    },
                    new Producto
                    {
                        Nombre = "Cámara",
                        Descripcion = "Cámara digital de alta resolución",
                        Precio = 400,
                        ImagenUrl = "gs://twecommerce-14b8f.appspot.com/Fotos_Perfil/camara.png",
                        CategoriaId = electronicaId
                    },
                    new Producto
                    {
                        Nombre = "Bici",
                        Descripcion = "Bicicleta de montaña",
                        Precio = 250,
                        ImagenUrl = "gs://twecommerce-14b8f.appspot.com/Fotos_Perfil/bici.png",
                        CategoriaId = deportesId
                    }
                };

                _context.Productos.AddRange(productos);
                _context.SaveChanges();
            }
        }
    }
}
