import { RouteInfo } from './sidebar.metadata';

export const ROUTES: RouteInfo[] = [
  {
    path: '',
    title: 'Personal',
    icon: 'mdi mdi-dots-horizontal',
    class: 'nav-small-cap',
    extralink: true,
    submenu: []
  },
  {
    path: '/home',
    title: 'Home',
    icon: 'mdi mdi-gauge',
    class: '',
    extralink: false,
    submenu: []
  }
];
