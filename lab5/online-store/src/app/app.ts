import { Component, inject, signal } from '@angular/core';
import { Navbar } from './components/navbar/navbar';
import { CategoryMenu } from "./components/category-menu/category-menu";
import { ProductList } from "./components/product-list/product-list";
import { ProductService } from './services/product-service';

@Component({
  selector: 'app-root',
  imports: [Navbar, CategoryMenu, ProductList],
  templateUrl: './app.html',
  styleUrl: './app.css'
})

export class App {
  protected readonly title = signal('online-store');
  service: ProductService = inject(ProductService);

  activeProducts = this.service.activeProducts;

  filterProduct(filters: string[]) {
    this.service.filterProducts(filters);
  }

  deleteProduct(productId: number) {
    this.service.deleteProduct(productId);
  }

}
