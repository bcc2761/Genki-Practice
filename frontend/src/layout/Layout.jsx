import "react"
import {SignIn, SignedIn, SignedOut, UserButton} from '@clerk/clerk-react'
import {Outlet, Link, Navigate} from 'react-router-dom'

export function Layout() {
    return <div className="app-layout">
        <header className="app-header">
            <div className="header-content">
                <h1>
                    Genki Practice Tool
                </h1>
                <nav>
                    <SignedIn>
                        <Link to="/">Generate Challenge</Link>
                        <Link to="/history">History</Link>
                        <UserButton/>
                    </SignedIn>
                </nav>

            </div>
        </header>

        <main className="app-main">
            <SignedOut>
                <Navigate to="/sign-in" replace /> // Redirect to sign-in if not signed in
            </SignedOut>
            <SignedIn>
                <Outlet /> // Take what's passed to layout component 
            </SignedIn>
        </main>
    </div>
}