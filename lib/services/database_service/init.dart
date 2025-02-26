import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

class DatabaseService {
  static final _databaseName = 'user_management.db';
  static final _databaseVersion = 1;
  
  static final String _tableName = "users";
  static final String _id = "id";
  static final String _username = "username";
  static final String _password = "password";
  static final String _email = "email";
  static final String _metadata = "metadata";

  static Database? _database;

  static Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _initDatabase();
    return _database!;
  }

  static Future<Database> _initDatabase() async {
    String path = join(await getDatabasesPath(), _databaseName);
    return await openDatabase(
      path,
      version: _databaseVersion,
      onCreate: (db, version) async {
        await db.execute('''
          CREATE TABLE $_tableName (
            $_id INTEGER PRIMARY KEY,
            $_username TEXT NOT NULL,
            $_password TEXT NOT NULL,
            $_email TEXT,
            $_metadata TEXT
          )
        ''');
        print('Database created!');
        // Insert default user
        await db.insert(_tableName, {
          _username: 'admin',
          _password: 'admin', // Consider hashing the password
          _email: 'admin@example.com',
        });
        print('Default user added!');
      },
    );
  }

  static Future<bool> validateUser(String username, String password) async {
    try {
      final db = await database;
      final List<Map<String, dynamic>> maps = await db.query(
        _tableName,
        where: '$_username = ? AND $_password = ?',
        whereArgs: [username, password],
      );
      return maps.isNotEmpty;
    } catch (e) {
      print('Error validating user: $e');
      return false;
    }
  }

  static Future<void> addUser(String username, String password, String email,{String metadata=''}) async {
    try {
      final db = await database;
      await db.insert(_tableName, {
        _username: username,
        _password: password, // Consider hashing the password
        _email: email,
        _metadata: metadata,
      });
    } catch (e) {
      print('Error adding user: $e');
    }
  }

  static Future<void> close() async {
    final db = _database;
    if (db != null) {
      await db.close();
    }
  }
}