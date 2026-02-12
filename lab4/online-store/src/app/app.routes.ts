import { Routes } from '@angular/router';
import { ProductList } from './components/product-list/product-list';
import { ProductCard } from './components/product-card/product-card';

export const routes: Routes = [
    {
        path: "",
        title: "Stuffs from Kaspi!!",
        component: ProductList,
    }
];
