import { Routes } from '@angular/router';
import { AboutComponent } from '../components/about-component/about-component';
import { AlbumPhotosComponent } from '../components/album-photos-component/album-photos-component';
import { AlbumsComponent } from '../components/albums-component/albums-component';
import { AlbumDetailsComponent } from '../components/album-details-component/album-details-component';
import { HomeComponent } from '../components/home-component/home-component';

export const routes: Routes = [
    { path: "", component: HomeComponent },
    { path: "about", component: AboutComponent },
    { path: "albums", component: AlbumsComponent },
    { path: "albums/:id", component: AlbumDetailsComponent },
    { path: "albums/:id/photos", component: AlbumPhotosComponent },
    { path: "**", redirectTo: "" },
];
