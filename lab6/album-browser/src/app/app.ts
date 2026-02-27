import { Component, computed, effect, inject, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Navbar } from '../components/navbar/navbar';
import { AlbumState } from '../services/album-state';
import { LoadingOverlayComponent } from '../components/loading-overlay-component/loading-overlay-component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, Navbar, LoadingOverlayComponent],
  templateUrl: './app.html',
  styleUrl: './app.css',
  standalone: true,
})
export class App {
  protected readonly title = signal('album-browser');
  albumState = inject(AlbumState);
  isLoading = computed(() => this.albumState.isFetchingData());
}
