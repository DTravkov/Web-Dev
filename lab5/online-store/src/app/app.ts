import { Component, inject, signal } from '@angular/core';
import { Navbar } from './components/navbar/navbar';
import { ProductList } from "./components/product-list/product-list";

@Component({
  selector: 'app-root',
  imports: [Navbar, ProductList],
  templateUrl: './app.html',
  styleUrl: './app.css'
})

export class App {
  protected readonly title = signal('online-store');

}
