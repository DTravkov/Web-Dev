import { computed, inject, Injectable, Signal, signal } from '@angular/core';
import { PRODUCTS } from '../../assets/products';
import { Product } from '../models/product.model';
import { StorageService } from './storage-service';
import { single } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ProductService {

  storageService: StorageService = inject(StorageService);

  activeFilters = signal<string[]>([]);

  rawProductListSignal = this.storageService.getRawProductListSignal();

  filteredProductList = computed(() =>
    this.rawProductListSignal().filter(
      prod => this.activeFilters().every(filt => Object.values(prod.category).includes(filt)))
  );

  getProductListSignal() {
    return this.filteredProductList;
  }


  filterProducts(newFilters: string[]) {
    this.activeFilters.set(newFilters);
  }

  likeProduct(productInstance: Product) {
    this.rawProductListSignal.update(arr => {
      return arr.map(prod => prod.id === productInstance.id ? { ...prod, likes: prod.likes + 1 } : prod);
    })
    this.storageService.save();
  }

  getLikesInfo(productInstance: Product) {
    const list = this.rawProductListSignal();
    const id = list.findIndex(prod => prod.id === productInstance.id);
    return list[id].likes;
  }

  deleteProduct(productInstance: Product) {
    this.storageService.remove(productInstance);
  }





}

