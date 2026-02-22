import { computed, Injectable, signal } from '@angular/core';
import { Product } from '../models/product.model';
import { PRODUCTS } from '../../assets/products';

@Injectable({
  providedIn: 'root',
})


export class StorageService {
  productList = signal<Product[]>(this.load());

  load() {
    const data = localStorage.getItem('productList');
    if (!data) return PRODUCTS;
    else {
      return JSON.parse(data);
    }

  }
  save() {
    localStorage.setItem('productList', JSON.stringify(this.productList()))
  }

  restoreDefaults() {
    this.productList.set([...PRODUCTS]);
    this.save();
  }

  add(newProduct: Product) {
    this.productList.update(arr => [...arr, newProduct]);
    this.save();
  }

  remove(productToDelete: Product) {
    this.productList.update(arr => arr.filter(prod => prod.id !== productToDelete.id));
    this.save();
  }

  update(newProductList: Product[]) {
    this.productList.set(newProductList);
    this.save();
  }

}
