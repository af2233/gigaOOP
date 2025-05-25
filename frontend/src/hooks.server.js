import { redirect } from '@sveltejs/kit';

/** @type {import('@sveltejs/kit').Handle} */

export async function handle({ event, resolve }) {
    const token = event.cookies.get('auth');

    console.log(`Token: ${token}`);
    console.log(`Pathname: ${event.url.pathname}`);
    console.log(`Headers: ${JSON.stringify(event.request.headers)}`);
    
    if (!token && event.url.pathname !== '/login') {
        console.log(`Redirecting to /login from ${event.url.pathname}`);
        redirect(307, '/login');
        
    }

    return resolve(event);
}
