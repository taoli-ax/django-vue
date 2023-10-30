<template>
    <div>
        <header>
            <div>
                <router-link to="/login">login</router-link>
            </div>
            <div>
                <router-link to="/signup">signup</router-link>
            </div>
            <div>
                <router-link to="/account">user center</router-link>
            </div>
            <div>
            <router-view/>
            </div>
            
           
        </header>
        <main>
            <aside>
                <dl>
                    <dt>cars</dt>
                    <dd><router-link to="/cars">all cars</router-link></dd>
                    <dd>customize</dd>
                </dl>
            </aside>

            <section>
                    <router-view name="carsinfo"/>
            </section>
        </main>
        <footer>
        </footer>
    </div>
</template>

<script>
export default{

}
</script>