import { Component, inject, signal } from '@angular/core';
import { Navbar } from './components/navbar/navbar';
import { CategoryMenu } from "./components/category-menu/category-menu";
import { ProductList } from "./components/product-list/product-list";
import { ProductService } from './services/product-service';
import { StorageService } from './services/storage-service';
import { Product } from './models/product.model';

@Component({
  selector: 'app-root',
  imports: [Navbar, CategoryMenu, ProductList],
  templateUrl: './app.html',
  styleUrl: './app.css'
})

export class App {
  protected readonly title = signal('online-store');

  productService: ProductService = inject(ProductService);
  storageService: StorageService = inject(StorageService);

  filterProduct(filters: string[]) {
    this.productService.filterProducts(filters);
  }

  likeProduct(productInstance: Product) {
    this.productService.likeProduct(productInstance);
  }

  deleteProduct(productInstance: Product) {
    this.storageService.remove(productInstance);
  }



}
