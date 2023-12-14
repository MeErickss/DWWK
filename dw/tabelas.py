from criacao import *
import sqlalchemy as sa
from sqlalchemy import Column, String, Integer, ForeignKey, Date, DateTime, Time, Float



def tables():

    engine = criar()[0]
    Base = criar()[1]
    session = criar()[3]


    sql = sa.text("""DROP TABLE IF EXISTS usuario,anuncio,anunciante,curtidas,seguidor,playlist,historico,artistas,ouvinte,musica CASCADE;""")
    engine.execute(sql)

    class usuario(Base):
        __tablename__ = "usuario"
        login = Column(String, primary_key=True)
        senha = Column(String, nullable=False)
        gmail = Column(String, nullable=False)
        data_criacao = Column(Date, nullable=False)
        def __repr__(self):
            return f'Atributos Pedidos: usuario({self.login},{self.senha},{self.gmail},{self.data_criacao})'


    class artistas(Base):
        __tablename__ = "artistas"
        id_art = Column(Integer, primary_key=True, autoincrement=True)
        login = Column(String, ForeignKey('usuario.login'))
        def __repr__(self):
            return f'Atributos Pedidos: artistas({self.id_art},{self.login})'


    class musica(Base):
        __tablename__ = "musica"
        id_msc = Column(Integer, primary_key=True, autoincrement=True)
        id_art = Column(Integer, ForeignKey('artistas.id_art'))
        nome = Column(String, nullable=False)
        data_lancamento = Column(DateTime, nullable=False)
        duracao = Column(Time, nullable=False)
        def __repr__(self):
            return f'Atributos Pedidos: musica({self.id_msc},{self.id_art},{self.nome},{self.data_lancamento},{self.duracao})'


    class seguidor(Base):
        __tablename__ = "seguidor"
        login_u = Column(String, ForeignKey('usuario.login'))
        login_seg = Column(String, ForeignKey('usuario.login'))
        id_seg = Column(Integer, primary_key=True, autoincrement=True)
        def __repr__(self):
            return f'Atributos Pedidos: seguidor({self.login_u},{self.login_seg})'


    class anuncio(Base):
        __tablename__ = "anuncio"
        id_anuncio = Column(Integer, primary_key=True)
        login = Column(String, ForeignKey('usuario.login'))
        frequencia = Column(Float, nullable=False)
        retencao = Column(Float, nullable=False)
        duracao = Column(Time, nullable=False)
        def __repr__(self):
            return f'Atributos Pedidos: anuncio({self.id_anuncio},{self.login},{self.frequencia},{self.retencao},{self.duracao})'


    class playlist(Base):
        __tablename__ = "playlist"
        login = Column(String, ForeignKey('usuario.login'))
        id_msc = Column(Integer, ForeignKey('musica.id_msc'))
        id_pla = Column(Integer, primary_key=True, autoincrement=True)
        def __repr__(self):
            return f'Atributos Pedidos: playlist({self.login},{self.id_msc})'


    class ouvinte(Base):
        __tablename__ = "ouvinte"
        login = Column(String, ForeignKey('usuario.login'))
        plano_mensal = Column(String, nullable=False)
        id_ouv = Column(Integer, primary_key=True, autoincrement=True)
        def __repr__(self):
            return f'Atributos Pedidos: ouvinte({self.login},{self.plano_mensal})'


    class curtidas(Base):
        __tablename__ = "curtidas"
        id_msc = Column(Integer, ForeignKey('musica.id_msc'))
        login = Column(String, ForeignKey('usuario.login'))
        id_cur = Column(Integer, primary_key=True, autoincrement=True)
        def __repr__(self):
            return f'Atributos Pedidos: curtidas({self.id_msc},{self.login})'


    class historico(Base):
        __tablename__ = "historico"
        login = Column(String, ForeignKey('usuario.login'))
        id_msc = Column(Integer, ForeignKey('musica.id_msc'))
        id_his = Column(Integer, primary_key=True, autoincrement=True)
        def __repr__(self):
            return f'Atributos Pedidos: historico({self.login},{self.id_msc})'


    class anunciante(Base):
        __tablename__ = "anunciante"
        login = Column(String, ForeignKey('usuario.login'))
        id_anuncio = Column(Integer, ForeignKey('anuncio.id_anuncio'))
        id_anu = Column(Integer, primary_key=True, autoincrement=True)
        def __repr__(self):
            return f'Atributos Pedidos: anunciante({self.login},{self.id_anuncio})'

    try:
        Base.metadata.create_all(criar()[0])
    except Exception as error:
        return error
        


    for i in range(10):
        if i == 0:
            session.add_all([
                            usuario(login='Pinguim12', senha='Xp7qZ9r2', gmail='Pinguim12@gmail.com', data_criacao='2023-10-08 14:30:00'),
                            usuario(login='Florr567', senha='Yv3tW5x8', gmail='Florr567@hotmail.com', data_criacao='2024-01-15 08:45:00'),
                            usuario(login='Girafa23', senha='Rf6mN1p3', gmail='Girafa23@gmail.com', data_criacao='2024-04-25 15:20:00'),
                            usuario(login='Elefante45', senha='Lc4eM5d9', gmail='Elefante45@yahoo.com', data_criacao='2024-07-12 12:10:00'),
                            usuario(login='Tigre90', senha='Kt1wU4y5', gmail='Tigre90@gmail.com', data_criacao='2025-02-20 09:55:00'),
                            usuario(login='Leao34', senha='Nv7Ys6r8', gmail='Leao34@outlook.com', data_criacao='2025-05-10 17:40:00'),
                            usuario(login='Zebra78', senha='Gw7Qx3s9', gmail='Zebra78@gmail.com', data_criacao='2025-08-30 13:25:00'),
                            usuario(login='Panda56', senha='Dm8Fy4R1', gmail='Panda56@hotmail.com', data_criacao='2026-03-18 10:15:00'),
                            usuario(login='Cachorro21', senha='Lw9Ks0t3', gmail='Cachorro21@gmail.com', data_criacao='2026-06-05 08:30:00'),
                            usuario(login='Gato77', senha='Nc6Gy1b0', gmail='Gato77@yahoo.com', data_criacao='2026-09-22 11:50:00'),
                            usuario(login='Papagaio10', senha='Xw6Zm1R3', gmail='Papagaio10@gmail.com', data_criacao='2027-02-15 16:05:00'),
                            usuario(login='Macaco88', senha='Fg2vHq4M', gmail='Macaco88@hotmail.com', data_criacao='2027-04-30 14:15:00'),
                            usuario(login='Coelho45', senha='Cz3Nv5t6', gmail='Coelho45@gmail.com', data_criacao='2027-08-10 09:40:00'),
                            usuario(login='Avestruz12', senha='Cv8Dp6D3', gmail='Avestruz12@yahoo.com', data_criacao='2027-11-25 18:00:00'),
                            usuario(login='Tartaruga56', senha='Ks1wRd5L', gmail='Tartaruga56@gmail.com', data_criacao='2028-02-02 07:15:00'), 
                            usuario(login='Cavalo33', senha='Hp2VcXw6', gmail='Cavalo33@outlook.com', data_criacao='2028-05-20 12:35:00'),
                            usuario(login='Gorila77', senha='Uq7RvXt5', gmail='Gorila77@gmail.com', data_criacao='2028-08-08 16:50:00'),
                            usuario(login='Pinguim127', senha='Hv8QwPc1', gmail='Pinguim12@yahoo.com', data_criacao='2029-01-28 15:10:00'),
                            usuario(login='Flamingo44', senha='Xz3JpMw2', gmail='Flamingo44@gmail.com', data_criacao='2029-04-12 10:25:00'),
                            usuario(login='Pato09', senha='Yj2RsBc6', gmail='Pato09@outlook.com', data_criacao='2029-07-22 09:05:00'),
                            usuario(login='Ganso20', senha='Ns2FwNv4', gmail='Ganso20@gmail.com', data_criacao='2029-10-05 14:55:00'),
                            usuario(login='Urso33', senha='Lp4HvXc2', gmail='Urso33@yahoo.com', data_criacao='2030-03-15 11:30:00'),
                            usuario(login='Peixe55', senha='Dw8YjRz5', gmail='Peixe55@gmail.com', data_criacao='2030-05-28 08:20:00'),
                            usuario(login='Golfinho23', senha='Cp4MzLq9', gmail='Golfinho23@hotmail.com', data_criacao='2030-10-09 17:15:00'),
                            usuario(login='Tubarao90', senha='Qr5TjSp2', gmail='Tubarao90@gmail.com', data_criacao='2031-01-11 15:45:00'),
                            usuario(login='Caranguejo08', senha='Xw3NzGv7', gmail='Caranguejo08@yahoo.com', data_criacao='2031-05-05 12:40:00'),
                            usuario(login='Lula78', senha='Gq9YwFp5', gmail='Lula78@gmail.com', data_criacao='2031-07-18 10:00:00'),
                            usuario(login='Polvo23', senha='Uv2DcRv1', gmail='Polvo23@outlook.com', data_criacao='2031-11-30 09:10:00'),
                            usuario(login='Baleia55', senha='Ez5NwBm8', gmail='Baleia55@gmail.com', data_criacao='2032-02-25 13:55:00'),
                            usuario(login='Orca12', senha='Zp4LwVc2', gmail='Orca12@yahoo.com', data_criacao='2032-06-18 16:30:00'),
                            usuario(login='Tubarao33', senha='Jm6WtHq3', gmail='Tubarao33@gmail.com', data_criacao='2032-09-22 14:05:00'),
                            usuario(login='Enguia45', senha='Lr2XvTp4', gmail='Enguia45@hotmail.com', data_criacao='2032-12-03 11:25:00'),
                            usuario(login='Salamandra08', senha='Dz3FtCn6', gmail='Salamandra08@gmail.com', data_criacao='2033-03-28 10:15:00'),
                            usuario(login='Cobra22', senha='Vz2CsMw9', gmail='Cobra22@yahoo.com', data_criacao='2033-06-09 08:50:00'),
                            usuario(login='Crocodilo11', senha='Tn9WmQw5', gmail='Crocodilo11@gmail.com', data_criacao='2033-11-19 17:20:00'),
                            usuario(login='Jacare09', senha='Gc6PvZp4', gmail='Jacare09@outlook.com', data_criacao='2032-12-03 11:25:00'),
                            usuario(login='Aranha76', senha='Dq2JwYv1', gmail='Aranha76@gmail.com', data_criacao='2032-12-03 11:25:00'),
                            usuario(login='Escorpiao88', senha='Yr9NwHs7', gmail='Escorpiao88@yahoo.com', data_criacao='2032-12-03 11:25:00'),
                            usuario(login='Libelula44', senha='Nv5MsYc6', gmail='Libelula44@gmail.com', data_criacao='2032-12-03 11:25:00')
                            ])
            session.commit()


        elif i == 1:
            session.add_all([
                            artistas(id_art=1, login='Urso33'),
                            artistas(id_art=2, login='Escorpiao88'),
                            artistas(id_art=3, login='Aranha76'),
                            artistas(id_art=4, login='Cobra22'),
                            artistas(id_art=5, login='Baleia55'),
                            artistas(id_art=6, login='Orca12'),
                            artistas(id_art=7, login='Crocodilo11'),
                            artistas(id_art=8, login='Lula78'),
                            artistas(id_art=9, login='Libelula44'),
                            artistas(id_art=10, login='Jacare09'),
                            artistas(id_art=11, login='Golfinho23'),
                            artistas(id_art=12, login='Peixe55')
                            ])
            session.commit()


        elif i == 2:
            session.add_all([
                            musica(id_msc=1, id_art=1,  nome='Canção da Natureza', data_lancamento='2033-06-09 08:50:00', duracao='03:45'),
                            musica(id_msc=2, id_art=2, nome='Noite Estrelada', data_lancamento='2033-07-15 14:20:00', duracao='04:12'),
                            musica(id_msc=3, id_art=3, nome='Teia de Sonhos', data_lancamento='2033-08-21 09:30:00', duracao='03:58'),
                            musica(id_msc=4, id_art=4, nome='Serpente Dançante', data_lancamento='2033-09-28 16:10:00', duracao='04:30'),
                            musica(id_msc=5, id_art=5, nome='Oceano Profundo', data_lancamento='2033-10-05 22:05:00', duracao='03:15'),
                            musica(id_msc=6, id_art=6, nome='Canção da Orca', data_lancamento='2033-11-12 05:40:00', duracao='03:48'),
                            musica(id_msc=7, id_art=7, nome='Lenda do Pântano', data_lancamento='2033-12-18 11:15:00', duracao='04:22'),
                            musica(id_msc=8, id_art=8, nome='No Fundo do Mar', data_lancamento='2034-01-25 17:55:00', duracao='03:59'),
                            musica(id_msc=9, id_art=9, nome='Voo da Libélula', data_lancamento='2034-02-03 23:30:00', duracao='04:10'),
                            musica(id_msc=10, id_art=10, nome='Ritmo do Crocodilo', data_lancamento='2034-03-11 07:20:00', duracao='03:38'),
                            musica(id_msc=11, id_art=11, nome='Canto do Golfinho', data_lancamento='2034-04-19 13:45:00', duracao='04:05'),
                            musica(id_msc=12, id_art=12, nome='Reino dos Peixes', data_lancamento='2034-05-27 19:18:00', duracao='03:30'),
                            musica(id_msc=13, id_art=1, nome='Canção da Natureza 2', data_lancamento='2034-06-09 08:50:00', duracao='03:30'),
                            musica(id_msc=14, id_art=4, nome='Estrela Cadente', data_lancamento='2034-07-15 14:20:00', duracao='04:15'),
                            musica(id_msc=15, id_art=3, nome='Sonhos Perdidos', data_lancamento='2034-08-21 09:30:00', duracao='04:05'),
                            musica(id_msc=16, id_art=4, nome='Dança das Serpentes', data_lancamento='2034-09-28 16:10:00', duracao='04:45'),
                            musica(id_msc=17, id_art=12, nome='Mar Profundo', data_lancamento='2034-10-05 22:05:00', duracao='03:25'),
                            musica(id_msc=18, id_art=11, nome='Canção da Baleia', data_lancamento='2034-11-12 05:40:00', duracao='03:40'),
                            musica(id_msc=19, id_art=11, nome='Mistérios do Pântano', data_lancamento='2034-12-18 11:15:00', duracao='04:35'),
                            musica(id_msc=20, id_art=12, nome='Aventuras Submarinas', data_lancamento='2035-01-25 17:55:00', duracao='03:50'),
                            musica(id_msc=21, id_art=9, nome='Voo da Libélula 2', data_lancamento='2035-02-03 23:30:00', duracao='04:20'),
                            musica(id_msc=22, id_art=10, nome='Ritmo do Crocodilo 2', data_lancamento='2035-03-11 07:20:00', duracao='03:55'),
                            musica(id_msc=23, id_art=11, nome='Sinfonia da Floresta', data_lancamento='2035-04-18 14:30:00', duracao='04:10'),
                            musica(id_msc=24, id_art=3, nome='Canção das Estrelas', data_lancamento='2035-05-25 09:15:00', duracao='03:40'),
                            musica(id_msc=25, id_art=4, nome='Melodia da Aurora', data_lancamento='2035-06-02 18:45:00', duracao='04:25'),
                            musica(id_msc=26, id_art=1, nome='Sussurros do Vento', data_lancamento='2035-07-09 03:20:00', duracao='03:58'),
                            musica(id_msc=27, id_art=11, nome='Balada das Marés', data_lancamento='2035-08-15 12:10:00', duracao='04:30'),
                            musica(id_msc=28, id_art=9, nome='Revoada de Pássaros', data_lancamento='2035-09-22 20:55:00', duracao='03:45'),
                            musica(id_msc=29, id_art=11, nome='Ritmica das Águas', data_lancamento='2035-10-29 07:30:00', duracao='03:15'),
                            musica(id_msc=30, id_art=1, nome='Canto da Montanha', data_lancamento='2035-11-04 14:25:00', duracao='03:55'),
                            musica(id_msc=31, id_art=4, nome='Harmonia da Selva', data_lancamento='2035-12-11 21:40:00', duracao='04:18'),
                            musica(id_msc=32, id_art=11, nome='Ciclo das Marés', data_lancamento='2036-01-17 05:05:00', duracao='04:42')
                            ])
            session.commit()


        elif i == 3:
            session.add_all([
                            seguidor(login_u='Pinguim12', login_seg='Florr567'),
                            seguidor(login_u='Pinguim12', login_seg='Girafa23'),
                            seguidor(login_u='Pinguim12', login_seg='Elefante45'),
                            seguidor(login_u='Florr567', login_seg='Girafa23')    
                            ])
            session.commit()


        elif i == 4:
            session.add_all([
                            anuncio(id_anuncio=1, login='Golfinho23', frequencia=3.14, retencao=3.162, duracao='00:00:05'),
                            anuncio(id_anuncio=2, login='Cachorro21', frequencia=2.71, retencao=2.236, duracao='00:00:10'),
                            anuncio(id_anuncio=3, login='Tartaruga56',  frequencia=1.4, retencao=0.577, duracao='00:00:15'),
                            anuncio(id_anuncio=4, login='Coelho45', frequencia=0.57, retencao=1.732, duracao='00:00:20')    
                            ])
            session.commit()
            

        elif i == 5:
            session.add_all([
                            playlist(login='Pinguim12', id_msc=2),
                            playlist(login='Florr567', id_msc=3),
                            playlist(login='Florr567', id_msc=4),
                            playlist(login='Girafa23', id_msc=5)    
                            ])
            session.commit()


        elif i == 6:
            session.add_all([
                            ouvinte(login='Pinguim12', plano_mensal='pago'),
                            ouvinte(login='Florr567', plano_mensal='gratis'),
                            ouvinte(login='Girafa23', plano_mensal='pago'),
                            ouvinte(login='Elefante45', plano_mensal='gratis')    
                            ])
            session.commit()


        elif i == 7:
            session.add_all([
                            curtidas(id_msc=1, login='Pinguim12'),
                            curtidas(id_msc=4, login='Pinguim12'),
                            curtidas(id_msc=6, login='Pinguim12'),
                            curtidas(id_msc=9, login='Pinguim12')    
                            ])
            session.commit()

        elif i == 8:
            session.add_all([
                            historico(login='Pinguim12', id_msc=1),
                            historico(login='Pinguim12', id_msc=4),
                            historico(login='Pinguim12', id_msc=7),
                            historico(login='Pinguim12', id_msc=10)
                            ])
            session.commit()



        elif i == 9:
            session.add_all([anunciante(login='Golfinho23', id_anuncio=1),
                            anunciante(login='Cachorro21', id_anuncio=2),
                            anunciante(login='Tartaruga56', id_anuncio=3),
                            anunciante(login='Coelho45', id_anuncio=4)
                            ])
            
            
    session.commit()
    return "População e criação de tabelas feita com sucesso!!!"