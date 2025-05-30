import asyncio

async def main():
    print("Hola, mundo!")
    await asyncio.sleep(1)
    print("Adiós, mundo!")

asyncio.run(main())

async def tarea():
    print("Tarea iniciada")
    await asyncio.sleep(2)
    print("Tarea finalizada")
