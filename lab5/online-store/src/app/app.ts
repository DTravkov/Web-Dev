import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Navbar } from './components/navbar/navbar';
import { PRODUCTS } from '../assets/products';
import { CategoryMenu } from "./components/category-menu/category-menu";
import { Product } from './models/product.model';
import { ProductList } from "./components/product-list/product-list";
import { filter } from 'rxjs';

@Component({
  selector: 'app-root',
  imports: [Navbar, CategoryMenu, ProductList],
  templateUrl: './app.html',
  styleUrl: './app.css'
})

export class App {
  protected readonly title = signal('online-store');

  allProducts = PRODUCTS;

  lastFilters: string[] = [];
  deletedIds: number[] = [];

  activeProducts = signal<Product[]>([]);

  handleFilterEvent(filters: string[]) {
    this.lastFilters = filters; // !-----
    const filtered = this.allProducts.filter(prod => {
      if (filters.every(filt => Object.values(prod.category).includes(filt))
        && !this.deletedIds.includes(prod.id)) {
        return true;
      }
      return false;
    }
    );
    this.activeProducts.set(filtered);
  }

  handleDeleteEvent(productId: number) {
    this.deletedIds.push(productId);
    this.handleFilterEvent(this.lastFilters);
  }



}
