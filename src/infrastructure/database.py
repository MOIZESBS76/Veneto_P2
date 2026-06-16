class MongoSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoSingleton, cls).__new__(cls)
            # Aqui entraria a lógica real de conexão com pymongo
            cls._instance.connection = "MongoDB_Active_Connection"
        return cls._instance