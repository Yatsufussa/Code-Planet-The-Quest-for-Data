from django.db import models


#1
class DataField(models.Model):
    NamesOfTheHacked = models.CharField(max_length=50, null=True)
    VirusName = models.CharField(max_length=50, null=True)
    CodeOfData = models.IntegerField(null=True)
    HackingTime = models.TimeField(null=True)

    # INSERT INTO game_app_datafield (NamesOfTheHacked, VirusName, CodeOfData, HackingTime) VALUES
    # ('Zafar', 'Cryptos', 1111111111, '12:15:00'),
    # ('Nikita', 'DATALOSS', 11001001, '18:15:45'),
    # ('Shahboz', 'ILOVEYOU', 10110, '01:01:10'),
    # ('Shukhrat', 'Meltdown', 10101011, '21:20:30');

#2
class LakeData(models.Model):
    LakeDatabase = models.CharField(max_length=50, null=True)
    NumberOfAbsorbedFiles = models.IntegerField(null=True)
    MainFile = models.CharField(max_length=50, null=True)
    InfectionTime = models.TimeField(null=True)

    # INSERT INTO game_app_LakeData (LakeDatabase, NumberOfAbsorbedFiles, MainFile,InfectionTime)
    # VALUES
    # ('BeautifulDb', 2, 'Vog.bat', '12:45:17'),
    # ('MyDbBroke', 523, 'Victory.txt',  '21:45:17'),
    # ('PureH2ODB', 3, 'Voron.jpg', '16:10:59'),
    # ('NasaDB', 22, 'Verticalspace.csv', '19:20:47');


#3
class Mountain_Of_Algorithms(models.Model):
    MountainName = models.CharField(max_length=255, null=True)
    WayOfTheMountain = models.CharField(max_length=255, null=True)
    PathLength = models.IntegerField(null=True)
    MountainKeeper = models.CharField(max_length=255, null=True)

    # INSERT INTO game_app_Mountain_Of_Algorithms (MountainName, WayofTheMountain, Pathlength, MountainKeeper)
    # VALUES
    # ('Bitonic', 'Quick', 245, 'Bubble'),
    # ('Selection', 'Hard', 4123, 'Shaker'),
    # ('Shell', 'Long', 25321, 'Sort'),
    # ('Insertion', 'rapidly', 421, 'Algorithm'),
    # ('Comb', 'Medium', 512, 'Radix');


#5
class Operator_Forest(models.Model):
    TrailId = models.IntegerField(primary_key=True)
    VirusName = models.CharField(max_length=255, null=True, default=None)
    FileName = models.CharField(max_length=255, null=True, default=None)
    FileWeight = models.IntegerField(null=True, default=None)
    Operator = models.CharField(max_length=255, null=True, default=None)

    # INSERT INTO game_app_Operator_Forest (TrailId, VirusName, FileName, FileWeight, Operator)
    # VALUES
    # (1, 'Cryptos', 'Choy.c', 112, '& or >'),
    # (2, 'ILOVEYOU', 'PANDA.py', 12, '& or <'),
    # (3, 'Meltdown', 'DataFile.doc', 56, '|| or >'),
    # (4, 'DATALOSS', 'Forest.txt', 29, '< or ||'),
    # (5, 'MyVirus', 'Code.py', 2003, '& or =');


#lvl 6-1
class PetaByte_Bay(models.Model):
    TableId = models.IntegerField(null=True)
    TableName = models.CharField(max_length=255, null=True)
    RecordDataKB = models.CharField(max_length=255, null=True)
    DataLoss = models.IntegerField(null=True)

    # INSERT
    # INTO
    # game_app_PetaByte_Bay(Tableid, TableName, RecordDataKB, DataLoss)
    # VALUES
    # (1, 'Hidden_Data', 'Contact_book * 1.6', 220),
    # (2, 'Request_log', '1040 - Contact_book', 100),
    # (3, 'Contact_book', '500', 20),
    # (4, 'Message_Archive', 'transaction_register / 0.2 - 1750', 125),
    # (5, 'Transaction_Register', 'request_log * 2', 10);

    #lvl6-2


class PetaByte_Bay2(models.Model):
    TableId = models.IntegerField(null=True)
    TableName = models.CharField(max_length=255, null=True)
    RecordDataKB = models.CharField(max_length=255, null=True)
    DataLoss = models.IntegerField(null=True)


    # INSERT INTO game_app_PetaByte_Bay2 (Tableid, TableName, RecordDataKB, DataLoss)
    # VALUES
    # (6, 'Orders', 'Contact_book - Transaction_log', 220),
    # (7, 'Transaction_log', '100', 100),
    # (8, 'Help_data', 'Orders * 2 - 200', 20),
    # (9, 'Customer_data', '40', 125),
    # (10, 'Archive_log', 'Customer_data / 0.09', 10);


# lvl 7
class Cipher_Hills(models.Model):
    EncryptionID = models.IntegerField(null=True, default=None)
    CoderName = models.CharField(max_length=255, null=True, default=None)
    KeyBit = models.IntegerField(null=True, default=None)
    Operator = models.CharField(max_length=255, null=True, default=None)
    VirusFound = models.CharField(max_length=255, null=True, default=None)

    # INSERT INTO game_app_Cipher_Hills (EncryptionID, CoderName, KeyBit, Operator, VirusFound)
    # VALUES
    # (1111, 'AES-256', 32, '-', 'CyberDragon'),
    # (1000, 'UTM-16', 4096, '&', 'CodeCobra'),
    # (0000, 'UTF-8', 8, '<', 'PixelPlague'),
    # (1110, 'RSA', 16, '>', 'ElectronicParasite'),
    # (1000, 'Blowfish', 4, '==', 'Discordia');


#8
class Index_Valley(models.Model):
    TheDataBase = models.CharField(max_length=255, null=True, default=None)
    IndexType = models.CharField(max_length=255, null=True, default=None)
    MainFile = models.CharField(max_length=255, null=True, default=None)
    FileContents = models.CharField(max_length=255, null=True, default=None)

    # INSERT INTO game_app_Index_Valley (TheDataBase, IndexType, MainFile, FileContents)
    # VALUES
    # ('FoodCount', 'eerTB', 'Btrade.py', 'PythonScriptforTrading'),
    # ('Nasa', 'hsaH', 'hashCode.c', 'Implementing Hash Code'),
    # ('Perfectum', 'euqinU', 'SecretProject.docx', 'Classified Research Findings'),
    # ('Travel', 'Spatial', 'StealthMode.exe', 'Stealth Mode Application'),
    # ('Gaming', 'deretsulC', 'DeepRedSea.pdf', 'Mysterious Depths of the Red Sea');


class Index_Valley2(models.Model):
    TheDataBase = models.CharField(max_length=255, null=True, default=None)
    IndexType = models.CharField(max_length=255, null=True, default=None)
    MainFile = models.CharField(max_length=255, null=True, default=None)
    FileContents = models.CharField(max_length=255, null=True, default=None)

    # INSERT INTO game_app_Index_Valley2 (TheDataBase, IndexType, MainFile, FileContents)
    # VALUES
    # ('Library', 'NonClustered', 'GoldenSunset.png', 'Golden Sunset'),
    # ('Ecommerce', 'Constraint', 'MoonlightSonata.doc', 'Musical Exploration'),
    # ('Hospital', 'Composite', 'NeonCityData.csv', 'Data Analysis of a Neon City'),
    # ('School', 'tnrmucoD', 'GalacticAdventure.txt', 'Journey the Galactic Frontier'),
    # ('Inventory', 'Text Search', 'Lovestory.c', 'Coding Love - Romantic Algorithms');


#9
class Optimization_Plateau(models.Model):
    IndexType = models.CharField(max_length=255, null=True, default=None)
    DataSize = models.IntegerField(null=True, default=None)
    ContaminatedDataKB = models.IntegerField(null=True, default=None)
    Operators = models.CharField(max_length=255, null=True, default=None)

    # INSERT INTO game_app_Optimization_Plateau (IndexType, DataSize, ContaminatedDataKB, Operators)
    # VALUES
    # ('partial', 5942, 2669, 'Add'),
    # ('unique', 6483, 1234, 'Substract'),
    # ('text-Full', 839, 5583, 'Multiply'),
    # ('Tree-B', 2792, 11245, 'Like'),
    # ('Simple', 1677, 10958, 'Some');


class Optimization_Plateau2(models.Model):
    IndexType = models.CharField(max_length=255, null=True, default=None)
    DataSize = models.IntegerField(null=True, default=None)
    ContaminatedDataKB = models.IntegerField(null=True, default=None)
    Operators = models.CharField(max_length=255, null=True, default=None)


    # INSERT INTO game_app_Optimization_Plateau2 (IndexType, DataSize, ContaminatedDataKB, Operators)
    # VALUES
    # ('Composite', 946, 1112, 'Or'),
    # ('non-Unique', 2818, 1354, 'Nor'),
    # ('Spatial grid', 5034, 8362, 'Exists'),
    # ('Index', 4677, 7177, 'Minus');


class Lunar_Landscape(models.Model):
    NumOfVirusLegion = models.CharField(max_length=255, null=True, default=None)
    NumOfDefeatedMinions = models.IntegerField(null=True, default=None)
    AccessKeyValue = models.CharField(max_length=255, null=True, default=None)
    ReleasedFiles = models.CharField(max_length=255, null=True, default=None)


    # INSERT INTO game_app_Lunar_Landscape (NumOfVirusLegion, NumOfDefeatedMinions, AccessKeyValue, ReleasedFiles)
    # VALUES
    # ('N2101', 585, 'R SA', 'Sunset_Memories.doc'),
    # ('FG242', 933, 'GB D', 'Journey_to_the_Stars.txt'),
    # ('HL234', 515, 'N NP', 'Secrets_of_the_Depths.pdf'),
    # ('DO190', 711, 'CD G', 'Echoes_of_Silence.wav');

class Lunar_Landscape2(models.Model):
    NumOfVirusLegion = models.CharField(max_length=255, null=True, default=None)
    NumOfDefeatedMinions = models.IntegerField(null=True, default=None)
    AccessKeyValue = models.CharField(max_length=255, null=True, default=None)
    ReleasedFiles = models.CharField(max_length=255, null=True, default=None)

    # INSERT INTO game_app_Lunar_Landscape2 (NumOfVirusLegion, NumOfDefeatedMinions, AccessKeyValue, ReleasedFiles)
    # VALUES
    # ('3045B', 694, 'B BA', 'Ripples_in_Time.pptx'),
    # ('0101R', 1124, 'R KA', 'Timeless_Treasures.xlsx'),
    # ('MM723', 202, 'RR S', 'Lost_and_Found.mp4'),
    # ('AA20A', 593, 'XY Z', 'Whispering_Winds.jpg');
