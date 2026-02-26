import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { RouterLinkActive } from '@angular/router';
@Component({
  selector: 'app-navbar',
  imports: [RouterLink, RouterLinkActive],
  templateUrl: './navbar.html',
  styleUrl: './navbar.css',
  standalone: true,
})
export class Navbar {
  buttons = [
    { name: 'Home', path: '' },
    { name: 'Albums', path: '/albums' },
    { name: 'About', path: '/about' },
  ]
}
