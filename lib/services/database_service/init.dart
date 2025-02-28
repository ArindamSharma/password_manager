import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import 'package:flutter_passwordapp/models/user.dart';
import 'package:flutter_passwordapp/models/vault.dart';
import 'package:flutter_passwordapp/models/item.dart';

class DatabaseService {
  static final _databaseName = 'user_management.db';
  static final _databaseVersion = 1;

  static Database? _database;

  static Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _initDatabase();
    return _database!;
  }

  static Future<void> refreshDatabase() async {
    String path = join(await getDatabasesPath(), _databaseName);
    if (await databaseExists(path)) {
      await deleteDatabase(path);
      print('Database deleted at path: $path');
    }
    _database = await _initDatabase();
  }
  
  static Future<Database> _initDatabase() async {
    String path = join(await getDatabasesPath(), _databaseName);
    print('Database path: $path');
    return await openDatabase(
      path,
      version: _databaseVersion,
      onCreate: (db, version) async {
        print('OnCreate Called');
        await db.execute('''
          CREATE TABLE ${User.tableName} (
            ${User.columnId} INTEGER PRIMARY KEY,
            ${User.columnUsername} TEXT NOT NULL,
            ${User.columnPassword} TEXT NOT NULL,
            ${User.columnEmail} TEXT,
            ${User.columnModifiedDATIME} DATETIME NOT NULL
          )
        ''');
        await db.execute('''
          CREATE TABLE ${Vault.tableName} (
            ${Vault.columnId} INTEGER PRIMARY KEY,
            ${Vault.columnTitle} TEXT NOT NULL,
            ${Vault.columnUserID} TEXT NOT NULL,
            ${Vault.columnDescription} TEXT,
            ${Vault.columnModifiedDATIME} DATETIME NOT NULL
          )
        ''');
        await db.execute('''
          CREATE TABLE ${Item.tableName} (
            ${Item.columnId} INTEGER PRIMARY KEY,
            ${Item.columnVaultId} TEXT NOT NULL,
            ${Item.columnTitle} TEXT NOT NULL,
            ${Item.columnUsername} TEXT NOT NULL,
            ${Item.columnPassword} TEXT NOT NULL,
            ${Item.columnMetadata} TEXT,
            ${Item.columnModifiedDATIME} DATETIME NOT NULL
          )
        ''');
        print('Database created!');
        // Insert default user
        await db.insert(User.tableName, {
          User.columnUsername: 'admin',
          User.columnPassword: 'admin', // Consider hashing the password
          User.columnEmail: 'admin@example.com',
          User.columnModifiedDATIME: DateTime.now().toString(),
        });
        print('Default user added!');
        // Insert detault Vault
        await db.insert(Vault.tableName, {
          Vault.columnTitle: 'Default Vault',
          Vault.columnUserID: '1',
          Vault.columnDescription: 'Default Vault Description',
          Vault.columnModifiedDATIME: DateTime.now().toString(),
        });
        print('Default Vault added!');
        // Insert default Item
        await db.insert(Item.tableName, {
          Item.columnVaultId: '1',
          Item.columnTitle: 'Default Item',
          Item.columnUsername: 'defaultusername',
          Item.columnPassword: 'defaultpassword',
          Item.columnMetadata: 'defaultmetadata',
          Item.columnModifiedDATIME: DateTime.now().toString(),
        });
        print('Default Item added!');
      },
    );
  }

  // static Future<void> printAllTables() async {
  //   final db = await database;
  //   final List<Map<String, dynamic>> tables = await db.rawQuery('SELECT name FROM sqlite_master WHERE type="table"');
  //   print('Tables in the database:');
  //   tables.forEach((table) {
  //     print(table['name']);
  //   });
  // }

  static Future<bool> validateUser(String username, String password) async {
    try {
      final db = await database;
      final List<Map<String, dynamic>> maps = await db.query(
        User.tableName,
        where: '${User.columnUsername} = ? AND ${User.columnPassword} = ?',
        whereArgs: [username, password],
      );
      return maps.isNotEmpty;
    } catch (e) {
      print('Error validating user: $e');
      return false;
    }
  }

  static Future<void> addUser(String username, String password, String email, String modifieddatime) async {
    try {
      final db = await database;
      // Get the current highest id in the table
      final List<Map<String, dynamic>> maps = await db.query(User.tableName, orderBy: '${User.columnId} DESC', limit: 1);
      final int lastId = maps.isNotEmpty ? maps.first[User.columnId] as int : 0;

      // Insert the user with the auto-generated id
      await db.insert(User.tableName, {
        User.columnId: lastId + 1,
        User.columnUsername: username,
        User.columnPassword: password, // Consider hashing the password
        User.columnEmail: email,
        User.columnModifiedDATIME: modifieddatime,        
      });
    } catch (e) {
      print('Error adding user: $e');
    }
  }

  static Future<void> addVaultEntry(Vault vault) async {
    try {
      final db = await database;
      // Get the current highest id in the table
      final List<Map<String, dynamic>> maps = await db.query(Vault.tableName, orderBy: '${Vault.columnId} DESC', limit: 1);
      final int lastId = maps.isNotEmpty ? maps.first[Vault.columnId] as int : 0;

      // Insert the vault entry with the auto-generated id
      await db.insert(Vault.tableName, vault.toMap()..[Vault.columnId] = lastId + 1);
    } catch (e) {
      print('Error adding vault entry: $e');
    }
  }

  static Future<List<Vault>> getVaultEntriesByUserId(String userid) async {
    try {
      final db = await database;
      final List<Map<String, dynamic>> maps = await db.query(
        Vault.tableName,
        where: '${Vault.columnUserID} = ?',
        whereArgs: [userid],
      );
      return List.generate(maps.length, (i) {
        return Vault.fromMap(maps[i]);
      });
    } catch (e) {
      print('Error retrieving vault entries: $e');
      return [];
    }
  }

  static Future<void> addItem(Item item) async {
    try {
      final db = await database;
      // Get the current highest id in the table
      final List<Map<String, dynamic>> maps = await db.query(Item.tableName, orderBy: '${Item.columnId} DESC', limit: 1);
      final int lastId = maps.isNotEmpty ? maps.first[Item.columnId] as int : 0;

      // Insert the item with the auto-generated id
      await db.insert(Item.tableName, item.toMap()..[Item.columnId] = lastId + 1);
    } catch (e) {
      print('Error adding item: $e');
    }
  }

  static Future<List<Item>> getItemsByVaultId(String vaultid) async {
    try {
      final db = await database;
      final List<Map<String, dynamic>> maps = await db.query(
        Item.tableName,
        where: '${Item.columnVaultId} = ?',
        whereArgs: [vaultid],
      );
      return List.generate(maps.length, (i) {
        return Item.fromMap(maps[i]);
      });
    } catch (e) {
      print('Error retrieving items: $e');
      return [];
    }
  }

  static Future<void> close() async {
    final db = _database;
    if (db != null) {
      await db.close();
    }
  }
}