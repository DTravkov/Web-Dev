import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Navbar } from './components/navbar/navbar';
import { PRODUCTS } from '../assets/products';
import { CategoryMenu } from "./components/category-menu/category-menu";
import { Product } from './models/product.model';
import { ProductList } from "./components/product-list/product-list";

@Component({
  selector: 'app-root',
  imports: [Navbar, CategoryMenu, ProductList],
  templateUrl: './app.html',
  styleUrl: './app.css'
})

export class App {
  protected readonly title = signal('online-store');

  allProducts = PRODUCTS;
  activeProducts = signal<Product[]>([]);

  handleFilterEvent(filters: string[]) {
    const filtered = this.allProducts.filter(prod =>
      filters.every(filt => Object.values(prod.category).includes(filt))
    );
    this.activeProducts.set(filtered);
  }

}
