# Definição e Implementação da Estratégia de Acesso ao Banco de Dados

## 1. Objetivo
Definir uma estratégia eficiente para acessar e gerenciar o banco de dados no **Sistema de Mérito Estudantil**, garantindo alta performance, segurança e fácil manutenção.

## 2. Arquitetura de Acesso
A estratégia de acesso ao banco de dados segue a arquitetura **DAO (Data Access Object)**, separando a lógica de negócios da lógica de persistência de dados. Isso facilita a manutenção do código e promove reusabilidade, além de tornar o sistema mais modular.

### Componentes:
1. **DAO (Data Access Object)**: Define a interface para realizar operações no banco de dados.
2. **DTO (Data Transfer Object)**: Objetos que transportam dados entre o backend e o banco de dados.
3. **JPA/Hibernate**: Ferramentas ORM (Object-Relational Mapping) que mapeiam classes Java para tabelas no banco de dados e eliminam a necessidade de escrever SQL manualmente.
4. **Connection Pooling**: Será utilizado um pool de conexões para melhorar o desempenho e evitar overhead de conexões repetitivas ao banco.

---

## 3. Tecnologias Utilizadas
- **JPA/Hibernate**: Para mapeamento objeto-relacional (ORM).
- **Spring Data JPA**: Para abstração das operações de persistência com menos código.
- **H2 Database (Desenvolvimento)**: Banco de dados embutido para testes locais.
- **MySQL (Produção)**: Banco de dados relacional utilizado no ambiente de produção.
- **Flyway**: Para versionamento de scripts de migração de banco de dados.

---

## 4. Implementação da Camada DAO

### 4.1 Interface DAO

Criar uma interface DAO genérica, que será usada para realizar operações CRUD:

```java
public interface GenericDAO<T> {
    T findById(Long id);
    List<T> findAll();
    T save(T entity);
    void update(T entity);
    void delete(T entity);
}
