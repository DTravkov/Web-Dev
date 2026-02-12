import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { App } from './app/app';
import { ProductList } from './app/components/product-list/product-list';


bootstrapApplication(App, appConfig)
  .catch((err) => console.error(err));

bootstrapApplication(ProductList, appConfig)
  .catch((err) => console.error(err));
