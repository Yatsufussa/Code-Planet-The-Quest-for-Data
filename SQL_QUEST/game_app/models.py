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


class Log_Desrt(models.Model):
    log = models.CharField(max_length=255, null=True, blank=True)
    FileName = models.CharField(max_length=255, null=True, blank=True)
    actions = models.CharField(max_length=255, null=True, blank=True)
    LastUpdate = models.DateTimeField(auto_now=True)


# INSERT
# INTO
# `Log_Desrt`(`Log`, `FileName`, `Actions`, `LastUpdate`)
# VALUES
# ('General Query ', 'Mygame.c', '       Select', '2024-03-21 09:30:45'),
# ('Slow Query', 'JustPic.jpg', '   Delete     ', '2023-11-05 03:15:20'),
# ('Error', 'HiProject.py', '   Update     ', '2024-01-11 14:45:33'),
# ('Binary', 'Destiny.pdf', '     Injection     ', '2024-05-14 01:55:08');


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


#LVL11
class PlanetDungeons(models.Model):
    tunnel_name = models.CharField(max_length=255, null=True, blank=True)
    tunnel_depth = models.IntegerField(null=True, blank=True)
    virus_infected_squad = models.CharField(max_length=255, null=True, blank=True)
    leader_name = models.CharField(max_length=255, null=True, blank=True)


# INSERT INTO `game_app_PlanetDungeons` (`tunnel_name`, `tunnel_depth`, `virus_infected_squad`, `leader_name`) VALUES
# ('THeUnion', 547, 'Archivists', 'Archivist'),
# ('MARTJOIN', 938, 'DataMainers', 'Mainer'),
# ('BADD', 549, 'DataKeepers', 'KeeperOfTheLight'),
# ('SELECTIONS', 990, 'SqlHelpers', 'DELETER');
class PlanetDungeons2(models.Model):
    tunnel_name = models.CharField(max_length=255, null=True, blank=True)
    tunnel_depth = models.IntegerField(null=True, blank=True)
    virus_infected_squad = models.CharField(max_length=255, null=True, blank=True)
    leader_name = models.CharField(max_length=255, null=True, blank=True)


# INSERT INTO game_app_PlanetDungeons2 (`tunnel_name`, `tunnel_depth`, `virus_infected_squad`, `leader_name`) VALUES
# ('Create', 682, 'Log Masters', 'Limon'),
# ('JUconnect', 952, 'HelpME', 'Diego'),
# ('Combine', 707, 'NightStalkers', 'User'),
# ('LinkinPark', 723, 'Geeks', 'Connect');


# 12
class ArchivesCity(models.Model):
    folder_id = models.IntegerField(null=True, blank=True)
    table_name = models.CharField(max_length=255, null=True, blank=True)
    num_of_events = models.IntegerField(null=True, blank=True)
    ascii_helper = models.CharField(max_length=255, null=True, blank=True)


class ArchivesCity2(models.Model):
    folder_id = models.IntegerField(null=True, blank=True)
    table_name = models.CharField(max_length=255, null=True, blank=True)
    num_of_events = models.IntegerField(null=True, blank=True)
    ascii_helper = models.CharField(max_length=255, null=True, blank=True)


#13
class QueryFactory(models.Model):
    fabrick_floor_name = models.CharField(max_length=255, null=True, blank=True)
    operator = models.CharField(max_length=255, null=True, blank=True)
    virus_request = models.CharField(max_length=255, null=True, blank=True)
    viral_request_removed = models.IntegerField(null=True, blank=True)


class QueryFactory2(models.Model):
    fabrick_floor_name = models.CharField(max_length=255, null=True, blank=True)
    operator = models.CharField(max_length=255, null=True, blank=True)
    virus_request = models.CharField(max_length=255, null=True, blank=True)
    viral_request_removed = models.IntegerField(null=True, blank=True)


# INSERT INTO `game_app_QueryFactory` (`fabrick_floor_name`, `operator`, `virus_request`, `viral_request_removed`) VALUES
# ('ban', 'and', 'Select data...', 43),
# ('distinct', 'equal', 'Count *...', 88),
# ('riskyFloor', 'minus', 'Insert into data...', 41),
# ('select', 'plus', '...Exists...', 36);
#
# INSERT INTO `game_app_QueryFactory2` (`fabrick_floor_name`, `Operator`, `virus_request`, `viral_request_removed`) VALUES
# ('garden', 'not equal', 'Where virus_id...', 10),
# ('virusdetection', 'more than', 'From null', 1),
# ('wetfloor', 'less than', 'Concat....', 15),
# ('null', 'or', 'TRIM \'... ', 66);


#14
class APIFields(models.Model):
    programmer_name = models.CharField(max_length=255, null=True, blank=True)
    method_request = models.CharField(max_length=255, null=True, blank=True)
    api = models.CharField(max_length=255, null=True, blank=True)
    virus_file_detected = models.CharField(max_length=255, null=True, blank=True)


class APIFields2(models.Model):
    programmer_name = models.CharField(max_length=255, null=True, blank=True)
    method_request = models.CharField(max_length=255, null=True, blank=True)
    api = models.CharField(max_length=255, null=True, blank=True)
    virus_file_detected = models.CharField(max_length=255, null=True, blank=True)


# INSERT INTO `game_app_APIFields` (`programmer_name`, `method_request`, `API`, `virus_file_detected`) VALUES
# ('riko', 'ajax', 'api.openweathermap.org', 'alpha.txt'),
# ('cago', 'axios', 'api.themoviedb.org', 'spreadsheet.xlsx'),
# ('tsop', 'jquery', 'api.github', 'choy_presentation.pptx'),
# ('striker', 'fetch', 'newsapi.org', 'mywork.c');
#
# INSERT INTO `game_app_APIFields2` (`programmer_name`, `method_request`, `API`, `virus_file_detected`) VALUES
# ('mario', 'open', 'api.stripe.com', 'me.png'),
# ('request', 'ruby', 'api.maps.googlemapis', 'gameover.py'),
# ('bug', 'java', 'api.twitter.com', 'kappa_database.sqlite'),
# ('python', 'xml', 'api.spotify.com', 'ny_budget.xlsx');

#15
class SecurityCastle(models.Model):
    part_of_lock = models.CharField(max_length=255, null=True, blank=True)
    functions = models.CharField(max_length=255, null=True, blank=True)
    num_of_data = models.IntegerField(null=True, blank=True)
    asiisafe = models.CharField(max_length=255, null=True, blank=True)


class SecurityCastle2(models.Model):
    part_of_lock = models.CharField(max_length=255, null=True, blank=True)
    functions = models.CharField(max_length=255, null=True, blank=True)
    num_of_data = models.IntegerField(null=True, blank=True)
    asiisafe = models.CharField(max_length=255, null=True, blank=True)


# INSERT INTO `game_app_SecurityCastle` (`PartOfLock`, `functions`, `NumOfData`, `ASIISafe`) VALUES
# ('Requestroom', 'rank', 415, '76'),
# ('Kitchen', 'sample', 321, '73'),
# ('Library', 'fetch', 567, '77'),
# ('Bathroom', 'save', 210, '73'),
# ('Livingroom', 'row_number', 1000, '84');
#
# INSERT INTO `game_app_SecurityCastle2` (`PartOfLock`, `functions`, `NumOfData`, `ASIISafe`) VALUES
# ('dataroom', 'rank', 15, '75'),
# ('bedroom', 'sample', 31, '66'),
# ('storeroom', 'fetch', 67, '23'),
# ('garage', 'save', 2110, '11');

#16

class ProcessingClouds(models.Model):
    cloud_name = models.CharField(max_length=50, null=True, blank=True)
    files_in_cloud = models.CharField(max_length=100, null=True, blank=True)
    virus_file_name = models.CharField(max_length=100, null=True, blank=True)
    functions = models.CharField(max_length=50, null=True, blank=True)


class ProcessingClouds2(models.Model):
    cloud_name = models.CharField(max_length=50, null=True, blank=True)
    files_in_cloud = models.CharField(max_length=100, null=True, blank=True)
    virus_file_name = models.CharField(max_length=100, null=True, blank=True)
    functions = models.CharField(max_length=50, null=True, blank=True)


# INSERT INTO `game_app_ProcessingClouds` (`cloud_name`, `files_in_cloud`, `virus_file_name`, `Functions`) VALUES
# ('AzureCloud', 'presentation.pptx', 'ransomware.exe', 'MIN'),
# ('MainCloud', 'video.mp4', 'adware.msi', 'UPPER'),
# ('IBM Cloud', 'document.docx', 'keylogger.sys', 'LOWER'),
# ('Safari', 'music.mp3', 'virus.scr', 'CONCAT');
#
# INSERT INTO `game_app_ProcessingClouds2` (`cloud_name`, `files_in_cloud`, `virus_file_name`, `Functions`) VALUES
# ('AWSCloud', 'data1.txt', 'trojan.exe', 'Select'),
# ('AVGCloud', 'report.pdf', 'worm.bat', 'COUNT'),
# ('GoogleCloud', 'image.png', 'spyware.dll', 'SUM'),
# ('YandexCloud', 'backup.zip', 'malware.js', 'MAX');
#17

class DatabaseDepths(models.Model):
    database_name = models.CharField(max_length=100, null=True, blank=True)
    lvl_of_database = models.IntegerField(null=True, blank=True)
    virus_found = models.CharField(max_length=100, null=True, blank=True)
    database_info = models.CharField(max_length=100, null=True, blank=True)


class DatabaseDepths2(models.Model):
    database_name = models.CharField(max_length=100, null=True, blank=True)
    lvl_of_database = models.IntegerField(null=True, blank=True)
    virus_found = models.CharField(max_length=100, null=True, blank=True)
    database_info = models.CharField(max_length=100, null=True, blank=True)


# INSERT INTO `game_app_DatabaseDepths` (`database_name`, `lvl_of_database`, `virus_found`, `database_info`) VALUES
# ('ObscureDepths', 1600, 'ROOTKIT', 'Replicated'),
# ('EclipsedData', 1900, 'SPYWARE', 'Fragmented'),
# ('MidnightMaze', 1750, 'Adware', 'Mirrored'),
# ('UmbralVault', 1850, 'WHORO', 'Normalized');
#
# INSERT INTO `game_app_DatabaseDepths2` (`database_name`, `lvl_of_database`, `virus_found`, `database_info`) VALUES
# ('ObscureDepths', 1600, 'ROOTKIT', 'Replicated'),
# ('EclipsedData', 1900, 'SPYWARE', 'Fragmented'),
# ('MidnightMaze', 1750, 'Adware', 'Mirrored'),
# ('UmbralVault', 1850, 'WHORO', 'Normalized');

#18

class CodeCodeksRidge(models.Model):
    storage_name = models.CharField(max_length=100, null=True, blank=True)
    virus_codes = models.CharField(max_length=100, null=True, blank=True)
    instruction = models.CharField(max_length=100, null=True, blank=True)
    storage_status = models.CharField(max_length=100, null=True, blank=True)


class CodeCodeksRidge2(models.Model):
    storage_name = models.CharField(max_length=100, null=True, blank=True)
    virus_codes = models.CharField(max_length=100, null=True, blank=True)
    instruction = models.CharField(max_length=100, null=True, blank=True)
    storage_status = models.CharField(max_length=100, null=True, blank=True)


# INSERT INTO `game_app_CodeCodeksRidge` (`storage_name`, `virus_codes`, `instruction`, `storage_status`) VALUES
# ('ARCHIVE', '0xFA13B7', 'Decrypt', 'ON'),
# ('VAULT', '0x8C2E9F', 'Encrypt', 'OFF'),
# ('UNI', '0x5D764A', 'Decrypt', 'OFF'),
# ('CODE', '0x2B1F8D', 'Analyze', 'OFF');
#
# INSERT INTO `game_app_CodeCodeksRidge2` (`storage_name`, `virus_codes`, `instruction`, `storage_status`) VALUES
# ('LOCKER', '0x9A6C3F', 'Analyze', 'OFF'),
# ('CRYPT', '0xE5FAB2', 'Decrypt', 'OFF'),
# ('THREAT', '0x1C7A9D', 'Encrypt', 'OFF'),
# ('CABINET', '0x3E6D5A', 'Analyze', 'ON');

#19


class DataManagementCenter(models.Model):
    section_name = models.CharField(max_length=255)
    main_database = models.CharField(max_length=255)
    legion_virus_names = models.CharField(max_length=255)
    safe_code = models.CharField(max_length=255)


class DataManagementCenter2(models.Model):
    section_name = models.CharField(max_length=255)
    main_database = models.CharField(max_length=255)
    legion_virus_names = models.CharField(max_length=255)
    safe_code = models.CharField(max_length=255)


# INSERT INTO `game_app_DataManagementCenter` (`section_name`, `main_database`, `legion_virus_names`, `safe_code`) VALUES
# ('SystemBunker', 'Backup Database', 'Virus.Cerberus', 'VAULT5566'),
# ('VirusArchive', 'Antivirus Database', 'Virus.Abyss', 'UNIO135N'),
# ('BackupRoom', 'LogDatabase', 'Virus.Shadow', 'PROTECT9900'),
# ('AntivirusProtectionCenter', 'Main Registrar', 'Virus.Reaper', 'SELE24CT'),
# ('DataProcessing Room', 'Event Database', 'Virus.Nemesis', 'ADD1532');
#
# INSERT INTO `game_app_DataManagementCenter2` (`section_name`, `main_database`, `legion_virus_names`, `safe_code`) VALUES
# ('Administrator Main Office', 'Central Database', 'Virus.TrojanHorse', 'TRESN'),
# ('DataStorage', 'Virus Database', 'Virus.WormEater', 'CO32Q678'),
# ('ServerRoom', 'Logging System', 'Virus.DarkMatter', 'JOIN9101'),
# ('Monitoring Hall', 'Personal Data Database', 'Virus.Nightmare', 'I124123'),
# ('SecretLaboratory', 'Password Vault', 'Virus.Phantom', 'SECURE3344');

#20
class FinalShowdown(models.Model):
    knowledge_of_sql = models.CharField(max_length=255, null=True, blank=True)
    virus_code = models.CharField(max_length=50, null=True, blank=True)
    main_virus = models.CharField(max_length=60, null=True, blank=True)
    virus_status = models.CharField(max_length=100, null=True, blank=True)


class FinalShowdown2(models.Model):
    knowledge_of_sql = models.CharField(max_length=255, null=True, blank=True)
    virus_code = models.CharField(max_length=50, null=True, blank=True)
    main_virus = models.CharField(max_length=60, null=True, blank=True)
    virus_status = models.CharField(max_length=100, null=True, blank=True)


# INSERT INTO `game_app_FinalShowdown` (`knowledge_of_sql`, `virus_code`, `main_virus`, `virus_status`) VALUES
# ('Basic SELECT Statements', '12DEL03', 'TROJANHOUSE', 'Active'),
# ('Intermediate JOIN Operations', 'LDE153', 'WORMEATER', 'Dormant'),
# ('Advanced Indexing Techniques', '01D02E2A', 'DARKMATTER', 'Active'),
# ('Master Database Design', 'CATE0932', 'PHANTOM', 'Active'),
# ('SQL Injection Prevention', 'TRUNA3F', 'CERBERUS', 'Neutralized');
#
# INSERT INTO `game_app_FinalShowdown2` (`knowledge_of_sql`, `virus_code`, `main_virus`, `virus_status`) VALUES
# ('Stored Procedures', 'DS241', 'ABYSS', 'Active'),
# ('Transaction Management', 'FORE1T5T', 'SHADOW', 'Dormant'),
# ('Advanced Subqueries', 'GG13SA', 'REAPER', 'Active'),
# ('Database Security Best Practices', '0110132', 'NEMESIS', 'Quarantined'),
# ('Data Warehousing Concepts', '01B0110S', 'ETEK', 'Active');


# INSERT INTO `game_app_ArchivesCity` (`folder_id`, `table_name`, `num_of_events`, `ascii_helper`) VALUES
# (1, 'application_logs', 9, '78-111-77-114-10'),
# (2, 'sensor_data_logs', 4, '109-107-101-121'),
# (3, 'audit_logs', 71, '89-84-114-117-101'),
# (4, 'access_logs', 0, '110-111-116-109-101');
#
# INSERT INTO `game_app_ArchivesCity2`(`folder_id`, `table_name`, `num_of_events`, `ascii_helper`) VALUES
# (1, 'user_logs', 9, '78-111-77-111-114-10'),
# (2, 'events_logs', 14, '86-73-82-85-83'),
# (3, 'error_logs', 7, '100-111'),
# (4, 'transaction_logs', 20, '96-10-8-11-11-14-21');


# INSERT INTO Level_PuzzleTable_Mapping (level_id, puzzle_table_id) VALUES
# (1, 1),
# (2, 1),
# (3, 1),
# (4, 1),
# (5, 1),
# (6, 1),
# (6, 2),
# (7, 1),
# (8, 1),
# (8, 3),
# (9, 1),
# (9, 2),
# (10, 1),
# (10, 2 );
#
#
# INSERT INTO PuzzleTable (name) VALUES
# ('DataField'),
# ('LakeData'),
# ('Mountain_Of_Algorithms'),
# ('Operator_Forest'),
# ('Petabyte_Bay'),
# ('Petabyte_Bay2'),
# ('Cipher_Hills'),
# ('Index_Valley'),
# ('Index_Valley2'),
# ('Optimization_Plateau'),
# ('Optimization_Plateau2'),
# ('Lunar_Landscape');
# ('Lunar_Landscape2');

# triggers
# DELIMITER //
# CREATE TRIGGER top_time_constraint BEFORE INSERT ON CompletionTime
# FOR EACH ROW
# BEGIN
#     IF NEW.top_time > NEW.medium_time THEN
#         SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Top time must be less than or equal to medium time';
#     END IF;
# END //
# DELIMITER ;
# DELIMITER //
# CREATE TRIGGER medium_time_constraint BEFORE INSERT ON CompletionTime
# FOR EACH ROW
# BEGIN
#     IF NEW.medium_time > NEW.bad_time THEN
#         SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Medium time must be less than or equal to bad time';
#     END IF;
# END //
# DELIMITER ;


class Player(models.Model):
    nickname = models.CharField(max_length=255, null=True)
    registration_time = models.DateTimeField(auto_now_add=True, null=True)
    p_level = models.IntegerField(null=True, blank=True)


class Level(models.Model):
    title = models.CharField(max_length=255)

class RetryAttempt(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    retry_count = models.IntegerField(default=0)
class PuzzleTable(models.Model):
    table_name = models.CharField(max_length=255)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)


#
class Pass(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    retry_count = models.IntegerField(default=0)
    stars = models.IntegerField(default=0)
    time = models.DurationField(null=True, blank=True)


class ExperiencePoints(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    points = models.IntegerField()


class Performance(models.Model):
    level = models.OneToOneField(Level, on_delete=models.CASCADE)  # lvl_id as foreign key
    top_time = models.DurationField()
    medium_time = models.DurationField()
    bad_time = models.DurationField()

# INSERT INTO game_app_Level (title) VALUES
# ('DataField'),
# ('LakeData'),
# ('Mountain_Of_Algorithms'),
# ('Log_Desert'),
# ('Operator_Forest'),
# ('Petabyte_Bay'),
# ('Cipher_Hills'),
# ('Index_Valley'),
# ('Optimization_Plateau'),
# ('Lunar_Landscape');
