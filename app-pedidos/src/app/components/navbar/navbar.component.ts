import { Component, AfterViewInit, OnInit } from '@angular/core';

import { Router, ActivatedRoute } from '@angular/router';
import * as jQuery from 'jquery';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  
  constructor() { }
  public title:string = 'App-Pedido';
  public toogle:boolean = false;
  public app_name: string = 'App-Pedidos';
  ngOnInit(): void {
   
  }

  showNavbar():void{
    jQuery('#wrapper').toggleClass("toggled");
  }

}
