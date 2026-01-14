import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import 'package:rudraksha/models/user.dart';
import 'package:rudraksha/models/vault.dart';
import 'package:rudraksha/models/item.dart';

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
        await _createTables(db);
        await _insertDefaultData(db);
      },
    );
  }

  static Future<void> _createTables(Database db) async {
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
    print('Tables created!');
  }

  static Future<void> _insertDefaultData(Database db) async {
    // Insert default user
    await db.insert(User.tableName, {
      User.columnUsername: "qwe",
      User.columnPassword: "qwe", // Consider hashing the password
      User.columnEmail: "arindam@gmail.com",
      User.columnModifiedDATIME: DateTime.now().toString(),
    });
    print('Default user added!');

    // Insert default Vault
    await db.insert(Vault.tableName, {
      Vault.columnId: 1,
      Vault.columnTitle: "Vault0",
      Vault.columnUserID: "arindam",
      Vault.columnDescription: "this is a sample description for default vault and can be deleted",
      Vault.columnModifiedDATIME: DateTime.now().toString(),
    });
    print('Default Vault added!');

    // Insert default Item
    await db.insert(Item.tableName, {
      Item.columnId: 1,
      Item.columnVaultId: 1,
      Item.columnTitle: "Item0",
      Item.columnUsername: "TestUserName",
      Item.columnPassword: "TestPassword",
      Item.columnMetadata: "{'key1':'value1','key2':'value2'}",
      Item.columnModifiedDATIME: DateTime.now().toString(),
    });
    print('Default Item added!');
  }

  // User Methods
  static Future<bool> addUser(String username, String password, String email) async {
    try {
      final db = await database;
      if (await checkUserExistance(username)) {
        print('User already exists: $username');
        return false;
      }
      await db.insert(User.tableName, {
        User.columnUsername: username,
        User.columnPassword: password, // Consider hashing the password
        User.columnEmail: email,
        User.columnModifiedDATIME: DateTime.now().toString(),
      });
      print('User added: $username');
      return true;
    } catch (e) {
      print('Error adding user: $e');
      return false;
    }
  }

  static Future<bool> checkUserExistance(String username) async {
    try {
      final db = await database;
      final List<Map<String, dynamic>> maps = await db.query(
        User.tableName,
        where: '${User.columnUsername} = ?',
        whereArgs: [username],
      );
      return maps.isNotEmpty;
    } catch (e) {
      print('Error checking user existence: $e');
      return false;
    }
  }

  static Future<bool> authorizeUser(String username, String password) async {
    try {
      final db = await database;
      final List<Map<String, dynamic>> maps = await db.query(
        User.tableName,
        where: '${User.columnUsername} = ? AND ${User.columnPassword} = ?',
        whereArgs: [username, password],
      );
      return maps.isNotEmpty;
    } catch (e) {
      print('Error authorizing user: $e');
      return false;
    }
  }

  static Future<void> deleteUser(int id) async {
    try {
      final db = await database;
      await db.delete(User.tableName, where: '${User.columnId} = ?', whereArgs: [id]);
      print('User deleted: $id');
    } catch (e) {
      print('Error deleting user: $e');
    }
  }

  // Vault Methods
  static Future<void> addVaultEntry(String title, String userId, String description) async {
    try {
      final db = await database;
      // Query the maximum vaultId
      final List<Map<String, dynamic>> result = await db.rawQuery('SELECT MAX(${Vault.columnId}) as maxId FROM ${Vault.tableName}');
      int newVaultId = (result.first['maxId'] ?? 0) + 1;

      await db.insert(Vault.tableName, {
        Vault.columnId: newVaultId,
        Vault.columnTitle: title,
        Vault.columnUserID: userId,
        Vault.columnDescription: description,
        Vault.columnModifiedDATIME: DateTime.now().toString(),
      });
      print('Vault added: $title with id: $newVaultId');
    } catch (e) {
      print('Error adding vault entry: $e');
    }
  }

  static Future<void> deleteVault(int id) async {
    try {
      final db = await database;
      await db.delete(Vault.tableName, where: '${Vault.columnId} = ?', whereArgs: [id]);
      print('Vault deleted: $id');
    } catch (e) {
      print('Error deleting vault: $e');
    }
  }

  static Future<void> updateVault(int id, String title, String description) async {
    try {
      final db = await database;
      await db.update(
        Vault.tableName,
        {
          Vault.columnTitle: title,
          Vault.columnDescription: description,
          Vault.columnModifiedDATIME: DateTime.now().toString(),
        },
        where: '${Vault.columnId} = ?',
        whereArgs: [id],
      );
      print('Vault updated: $id');
    } catch (e) {
      print('Error updating vault: $e');
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

  // Item Methods
static Future<void> addItem(int vaultId, String title, String username, String password, String metadata) async {
  try {
    final db = await database;
    // Query the maximum itemId
    final List<Map<String, dynamic>> result = await db.rawQuery('SELECT MAX(${Item.columnId}) as maxId FROM ${Item.tableName}');
    int newItemId = (result.first['maxId'] ?? 0) + 1;

    await db.insert(Item.tableName, {
      Item.columnId: newItemId,
      Item.columnVaultId: vaultId,
      Item.columnTitle: title,
      Item.columnUsername: username,
      Item.columnPassword: password,
      Item.columnMetadata: metadata,
      Item.columnModifiedDATIME: DateTime.now().toString(),
    });
    print('Item added: $title with id: $newItemId');
  } catch (e) {
    print('Error adding item: $e');
  }
}

  static Future<void> deleteItem(int id) async {
    try {
      final db = await database;
      await db.delete(Item.tableName, where: '${Item.columnId} = ?', whereArgs: [id]);
      print('Item deleted: $id');
    } catch (e) {
      print('Error deleting item: $e');
    }
  }

  static Future<void> updateItem(int id, String title, String username, String password, String metadata) async {
    try {
      final db = await database;
      await db.update(
        Item.tableName,
        {
          Item.columnTitle: title,
          Item.columnUsername: username,
          Item.columnPassword: password,
          Item.columnMetadata: metadata,
          Item.columnModifiedDATIME: DateTime.now().toString(),
        },
        where: '${Item.columnId} = ?',
        whereArgs: [id],
      );
      print('Item updated: $id');
    } catch (e) {
      print('Error updating item: $e');
    }
  }

  static Future<List<Item>> getItemsByVaultId(int vaultid) async {
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
      print('Database closed');
    }
  }
}