#import
import asyncio


async def tarea():
    print("Tarea iniciada")
    await asyncio.sleep(2)  # Simula una tarea que toma tiempo
    print("Tarea finalizada")


async def main():
    print("Inicio del programa")
    await tarea()  # Llama a la tarea asincrónica
    print("Fin del programa")

async def tarea_paralelo():
    tarea_1 = asyncio.create_task(tarea()) # Crea una tarea asincrónica
    main_1 = asyncio.create_task(main())

    await asyncio.gather(tarea_1, main_1)

asyncio.run(tarea_paralelo()) #! Para poder ejecutar la función asincrónica