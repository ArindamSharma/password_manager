import 'package:shelf/shelf.dart';
import 'package:shelf_router/shelf_router.dart';
import 'package:shelf_static/shelf_static.dart';

class Routes {
  Router get router {
    final router = Router();

    // Serve static files from the 'public' directory
    final staticHandler = createStaticHandler('public', defaultDocument: 'index.html');
    router.get('/<file|.*>', staticHandler);

    // Define a route for user data
    router.get('/api/user/<id>', (Request request, String id) {
      return Response.ok('User ID: $id');
    });

    return router;
  }
}